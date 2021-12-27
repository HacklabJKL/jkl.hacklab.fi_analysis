# Read relevant post data from Wordpress export XML file to TinyDB json database 

# Requirements (written on Python 3.10.1)
# - pip install beautifulsoup4 lxml tinydb

from bs4 import BeautifulSoup
from tinydb import TinyDB, Query, table
import re


db = TinyDB('hacklabjkl-blog.json', sort_keys=True, indent=4, separators=(',', ': '))
db.default_table_name = 'wp_posts'

# Reading the data inside the xml file to a variable under the name
# data
with open('hacklabjyvskyl.WordPress.2021-12-26.xml', 'r') as f:
    data = f.read()
 
# Passing the stored data inside the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")
 
# Finding all instances of tag `unique`
b_posts = Bs_data.find_all('item')

for b_post in b_posts:
    post_id = b_post.find('wp:post_id').get_text()
    post_url = b_post.find('guid').get_text()
    post_title = b_post.find('title').get_text()
    
    post_content_html = b_post.find('content:encoded').get_text()  # strips html and cdata tags
    post_content = BeautifulSoup(post_content_html, "lxml").get_text().replace('\n',' ')  # strips newlines
    post_content = re.sub(r'\[/?caption[^\]]*?\]', '', post_content) # strips shortcodes
    
    post_excerpt_html = b_post.find('excerpt:encoded').get_text()
    post_excerpt = BeautifulSoup(post_excerpt_html, "lxml").get_text().replace('\n',' ')

    post_date = b_post.find('wp:post_date').get_text()
    post_type = b_post.find('wp:post_type').get_text()

    Document = Query()

    db.insert(table.Document({
        'id': post_id,
        'url': post_url,
        'title': post_title,
        'content': post_content,
        'excerpt': post_excerpt,
        'date': post_date,
        'type': post_type,
    }, doc_id = post_id))