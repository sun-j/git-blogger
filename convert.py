# this function returns all of the files in a given folder as a md
import os 
import markdown
from config import blog_path

def convert(): 
    posts = os.listdir(blog_path)

    page_html = ''

    for post in posts: 
        with open(blog_path + '/' + post) as f:
            text = f.read()
            page_html = page_html + markdown.markdown(text)
            page_html = page_html + "\n <br>"
        
    return page_html