"""
This script extracts blog titles and content from a list of URLs and saves them as text files using the OpenAI API.
"""

import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
env_path = '/Users/acrobat/Documents/GitHub/extract_html/.env'
load_dotenv(env_path)

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

SAVE_DIR = '/Users/acrobat/Documents/GitHub/extract_html/blogs'

def read_urls(file_path):
    """Read the URLs from the given text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def extract_content_from_html(html_code):
    """
    Extract the title and content from the given HTML code using OpenAI's language model.
    
    Args:
        html_code (str): The HTML source code of a blog post.

    Returns:
        str: The extracted title and content formatted in markdown.
    """
    prompt = f"""
    I will provide you with the HTML source code of a blog post. Your task is to extract the blog title and content from this HTML in markdown.

    Here is the HTML source:
    <html_source>
    {html_code}
    </html_source>

    Please follow these steps:
    1. Extract the text between the <title> tags. This is the blog title.
    2. Locate the main content section of the blog, usually within <div> or <article> tags, possibly identified by class or id attributes. Extract all text from this section, ignoring HTML tags.
    3. Format the response as follows:

    **Title:** [Blog Title Here]

    **Content:** [Blog Content Here]

    Do not include any other text, HTML tags, or content in your response. Only include the blog title and content as markdown, formatted as specified above.
    """
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o",
    )
    
    return chat_completion['choices'][0]['message']['content'].strip()

def save_content_to_file(title, content, save_dir):
    """
    Save the extracted content to a text file.

    Args:
        title (str): The title of the blog post.
        content (str): The content of the blog post.
        save_dir (str): The directory where the file should be saved.
    """
    if ' | Colgate' in title:
        title = title.split(' | Colgate')[0]

    filename = title.lower().replace(' ', '_') + '.txt'

    with open(os.path.join(save_dir, filename), 'w', encoding='utf-8') as file:
        file.write(title + '\n\n')
        file.write(content)

    print(f"Article saved as '{filename}'")

def main():
    urls = read_urls('/Users/acrobat/Documents/GitHub/extract_html/website_list.txt')

    for url in urls:
        try:
            # Fetch the HTML code
            url_response = requests.get(url, timeout=5)
            html_code = url_response.text

            # Extract content using the LLM
            extracted_content = extract_content_from_html(html_code)

            # Extract title and content from LLM response
            title_start = extracted_content.find("**Title:**") + len("**Title:**")
            content_start = extracted_content.find("**Content:**")

            title = extracted_content[title_start:content_start].strip()
            content = extracted_content[content_start + len("**Content:**"):].strip()

            # Save the content to a file
            save_content_to_file(title, content, SAVE_DIR)

        except requests.RequestException as req_err:
            print(f"Request error processing {url}: {req_err}")
        except Exception as e:
            print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    main()
