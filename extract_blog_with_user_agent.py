import os
import re
import requests
from bs4 import BeautifulSoup

# Define the directory to save the files
save_dir = '/Users/acrobat/Documents/GitHub/extract_html/blogs'

# Create the save directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Define headers to include User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Read the URLs from the text file
with open('/Users/acrobat/Documents/GitHub/extract_html/website_list.txt', 'r') as file:
    urls = file.read().splitlines()

# Define the stop phrase
stop_phrase = "Oral Care Center articles are reviewed by an oral health medical professional."

# Function to clean the filename
def clean_filename(filename):
    return re.sub(r'[^a-zA-Z0-9]+', '_', filename).strip('_')

# Function to extract content from Colgate format
def extract_colgate_content(soup):
    content_div = soup.find('div', class_='contentDrawer')
    if not content_div:
        content_div = soup.find('div', class_='article-main-container')
    content_text = []
    stop = False
    if content_div:
        for element in content_div.find_all(['p', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']):
            if stop_phrase in element.get_text():
                stop = True
                break
            if element.name == 'p':
                content_text.append(element.get_text().strip())
            elif element.name == 'h2':
                content_text.append(f"## {element.get_text().strip()}")
            elif element.name == 'h3':
                content_text.append(f"### {element.get_text().strip()}")
            elif element.name == 'h4':
                content_text.append(f"#### {element.get_text().strip()}")
            elif element.name == 'h5':
                content_text.append(f"##### {element.get_text().strip()}")
            elif element.name == 'h6':
                content_text.append(f"###### {element.get_text().strip()}")
            elif element.name == 'li':
                content_text.append(f"- {element.get_text().strip()}")
    return content_text

# Function to extract content from ADA format
def extract_ada_content(soup):
    content_div = soup.find('div', class_='content-placeholder')
    content_text = []
    stop = False
    if content_div:
        for element in content_div.find_all(['p', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']):
            if stop_phrase in element.get_text():
                stop = True
                break
            if element.name == 'p':
                content_text.append(element.get_text().strip())
            elif element.name == 'h2':
                content_text.append(f"## {element.get_text().strip()}")
            elif element.name == 'h3':
                content_text.append(f"### {element.get_text().strip()}")
            elif element.name == 'h4':
                content_text.append(f"#### {element.get_text().strip()}")
            elif element.name == 'h5':
                content_text.append(f"##### {element.get_text().strip()}")
            elif element.name == 'h6':
                content_text.append(f"###### {element.get_text().strip()}")
            elif element.name == 'li':
                content_text.append(f"- {element.get_text().strip()}")
    return content_text

# Process each URL
for url in urls:
    try:
        # Fetch the HTML code with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        html_code = response.text

        # Parse the HTML code
        soup = BeautifulSoup(html_code, 'html.parser')

        # Extract the title
        title = soup.find('title').text.strip()
        if ' | ' in title:
            title = title.split(' | ')[0]

        # Clean the title to be used as the filename
        filename = clean_filename(title.lower()) + '.txt'

        # Extract the content based on the format
        if 'colgate' in url:
            content_text = extract_colgate_content(soup)
        else:
            content_text = extract_ada_content(soup)

        # Join the content text into a single string
        content = '\n\n'.join(content_text)

        # Create a text file and write the title and content in markdown format
        with open(os.path.join(save_dir, filename), 'w', encoding='utf-8') as file:
            file.write(f"**Title:** {title}\n\n**Content:**\n\n{content}")

        print(f"Article saved as '{filename}'")

    except requests.RequestException as e:
        print(f"Failed to fetch the URL {url}: {e}")
    except Exception as e:
        print(f"An error occurred while processing the URL {url}: {e}")
