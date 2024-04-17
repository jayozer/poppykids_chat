import os
import requests
from bs4 import BeautifulSoup

# Define the directory to save the files
save_dir = '/Users/acrobat/Documents/GitHub/extract_html/blogs'

# Read the URLs from the text file
with open('/Users/acrobat/Documents/GitHub/extract_html/website_list.txt', 'r') as file:
    urls = file.read().splitlines()

# Process each URL
for url in urls:
    # Fetch the HTML code
    response = requests.get(url)
    html_code = response.text

    # Parse the HTML code
    soup = BeautifulSoup(html_code, 'html.parser')

    # Extract the title
    title = soup.title.string

    # If 'Colgate' is in the title, only use the part before ' | Colgate'
    if ' | Colgate' in title:
        title = title.split(' | Colgate')[0]

    # Modify the title to be used as the filename
    filename = title.lower().replace(' ', '_') + '.txt'

    # Extract the content
    content_div = soup.find('div', class_='article-main-container')
    content = ""
    for element in content_div.find_all(['p', 'li', 'h2']):
        if element.name == 'p':
            content += element.get_text(separator='\n') + '\n'
        elif element.name == 'li':
            content += '• ' + element.get_text() + '\n'
        elif element.name == 'h2':
            content += '\n' + element.get_text() + '\n'

    # Create a text file and write the title and content
    with open(os.path.join(save_dir, filename), 'w', encoding='utf-8') as file:
        file.write(title + '\n\n')
        file.write(content)

    print(f"Article saved as '{filename}'")