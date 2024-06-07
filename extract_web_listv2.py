import os
import requests
from bs4 import BeautifulSoup

# Define the directory to save the files
save_dir = '/Users/acrobat/Documents/GitHub/extract_html/blogs'

# Create the save directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Read the URLs from the text file
with open('/Users/acrobat/Documents/GitHub/extract_html/website_list.txt', 'r') as file:
    urls = file.read().splitlines()

# Process each URL
for url in urls:
    try:
        # Fetch the HTML code
        response = requests.get(url)
        response.raise_for_status()
        html_code = response.text

        # Parse the HTML code
        soup = BeautifulSoup(html_code, 'html.parser')

        # Extract the title
        title = soup.find('title').text.strip()

        # If 'Colgate' is in the title, only use the part before ' | Colgate'
        if ' | Colgate' in title:
            title = title.split(' | Colgate')[0]

        # Modify the title to be used as the filename
        filename = title.lower().replace(' ', '_') + '.txt'

        # Extract the main content
        main_content_div = soup.find('div', class_='contentDrawer base responsivegrid aem-GridColumn aem-GridColumn--default--12')
        content_text = []
        
        if main_content_div:
            for element in main_content_div.find_all(['p', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']):
                content_text.append(element.get_text().strip())

        # Join the content text into a single string
        content = '\n\n'.join(content_text)

        # Create a text file and write the title and content
        with open(os.path.join(save_dir, filename), 'w', encoding='utf-8') as file:
            file.write(f"Title:\n{title}\n\nContent: \n {content}")

        print(f"Article saved as '{filename}'")

    except requests.RequestException as e:
        print(f"Failed to fetch the URL {url}: {e}")
    except Exception as e:
        print(f"An error occurred while processing the URL {url}: {e}")
