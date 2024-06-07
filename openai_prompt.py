# Prompt: 
"""
I will provide you with the HTML source code of a blog post. Your task is to extract the blog title and content from this HTML in markdown.

Here is the HTML source:
<html_source>
{{HTML_SOURCE}}
</html_source>

Please follow these steps:
1. Extract the text between the <title> tags. This is the blog title.
2. Locate the main content section of the blog, usually within <div> or <article> tags, possibly identified by class or id attributes. Extract all text from this section, ignoring HTML tags.
3. Format the response as follows:

**Title:** [Blog Title Here]

**Content:** [Blog Content Here]

Do not include any other text, HTML tags, or content in your response. Only include the blog title and content as markdown, formatted as specified above.

"""