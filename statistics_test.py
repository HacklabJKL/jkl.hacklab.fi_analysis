# Demo script for reading data file, useful starting point

# Requirements (written on Python 3.10.1)
# - pip install tinydb
# https://tinydb.readthedocs.io

from tinydb import TinyDB, Query

db = TinyDB('data/hacklabjkl-blog.json', sort_keys=True, indent=4, separators=(',', ': '))
db.default_table_name = 'wp_posts'
Document = Query()

posts_table = db.table('wp_posts')

print(f'{len(posts_table)} posts total')

for post in posts_table:
    print(f"read {post['id']}")
