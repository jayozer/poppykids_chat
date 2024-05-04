# PoppyChat

## Data Preparation:
### Workflow Steps

1. **Run `extract_web_list.py`**
   - **Inputs**: `website_list.txt` (contains a list of websites)
   - **Processes**: Extracts content from the websites listed in `website_list.txt`
   - **Outputs**: Text files saved in the `blogs` folder

2. **Execute `convert_to_QA.ipynb` Notebook**
   - **Inputs**: Text files from the `blogs` folder
   - **Processes**: Generates Q&A pairs using LangChain
   - **Outputs**: `faq_training.txt` (contains Q&A pairs)

3. **Final Output**
   - The Q&A pairs stored in `faq_training.txt` can be used for training models or other purposes.

```
          extract_web_list.py      convert_to_QA.ipynb
Website List ─────────────> Text Files ─────────────> Q&A Pairs
   (website_list.txt)            (blogs folder)          (faq_training.txt)
```


#### Notes and Future improvements:
- Ideally, this notebook can be converted to a .py script that works with `extract_web_list.py`.
- The reason for choosing to separate this portion as a Jupyter notebook is the format of extracted webpages.
- `Extract_web_list` will run on Colgate Blogs, and other blogs such as Poppy will be manually added to the blogs folder.
- Future work can be to create a Webflow CMS extract to get Poppy blogs automatically, but this is not in scope for this project.
- `z_scraped_list.txt` keeps the list of already processed website links
- `prompt_template.txt` has the langchain HUMAN_TEMPLATE. CONTEXT is provided by the converted blog posts
- `list_of_source_websites.txt


# Next is to convert the `faq_training.txt` file to a format that can be used to train MIstral 7B Instruct.
