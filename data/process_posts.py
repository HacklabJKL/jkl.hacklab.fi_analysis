# Process posts with Neuwo.ai API saving response data to TinyDB

# Requirements (written on Python 3.10.1)
# - pip install beautifulsoup4 lxml tinydb requests
# Neuwo API Key defined as environment variable (commercially available via https://neuwo.ai)

from tinydb import TinyDB, Query

from os import environ
import requests 

API_KEY = environ['NEUWO_TOKEN']

db = TinyDB('hacklabjkl-blog.json', sort_keys=True, indent=4, separators=(',', ': '))
db.default_table_name = 'wp_posts'

Document = Query()

publication_id = 'hacklabjkl-test'

def neuwo_get_ai_topics(post):
    '''Get Neuwo keywords from /getAiTopics endpoint'''

    req_data = {
            'documentid': publication_id + '_' + str(post.doc_id),
            'publicationid': publication_id,
            'content': post['content'],
            'format': 'json',
            # 'lang': 'fi',  # gets autodetected, better as there's mixed language posts
    }
  
    resp = requests.post('https://m1api.neuwo.ai/GetAiTopics', params={"token": API_KEY}, data=req_data)

    if not resp.status_code == 200:
        print('Encountered Neuwo API problem')
        breakpoint()

    data = resp.json()
    post['neuwo_data'] = data
    db.upsert(post)


posts_table = db.table('wp_posts')

for post in posts_table:
    if not post.get('neuwo_data'):
        print(f"Fetching Neuwo.io keyword data for post {post['id']}")
        neuwo_get_ai_topics(post)
    else:
        print(f"Skipped post {post['id']} with existing Neuwo.io keyword data")
