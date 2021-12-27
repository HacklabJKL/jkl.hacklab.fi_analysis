# Dataset description

WordPress eXtended RSS file `hacklabjyvskyl.WordPress.2021-12-26.xml` exported via Wordpress Admin Panel Tools > Export including all post data is converted by `load_posts.py` into `/data/hacklabjkl-blog.json` TinyDB json database file. Original XML file not included in repository as it contains irrelevant and possibly private data such as blog author email addresses.

Database file is processed in `process_posts.py` via [Neuwo.ai](https://neuwo.ai) [API](https://neuwo.ai/rest-api/) `/getAiTopics` providing Finnish/English NLP keyword analysis that is stored in `neuwo_data` key.

There was Unicode UTF-8 encoding problems on Mac, replaced \u00f6 \u00e4 characters with ö and ä on text editor.

neuwo_data json key contains:

- tags: Keywords in Finnish
    - value: tag name
    - score: relevance score in decimal 0-1
    - URI: Neuwo side url for tag, not useful for now
- marketing_categories: IAB 2.2 content taxonomy, international standard format for content categorization in two levels (tiers) https://iabtechlab.com/standards/content-taxonomy/
    - label: IAB taxonomy label
    - ID
    - relevance: relevance score in decimal 0-1
- brand_safety: used for marketing purposes, something like indicating nsfw-content

# Ideas

- Create summary statistics and visualizations (tag cloud etc) from Neuwo data
- Defining useful taxonomy structure for the Hacklab Jkl blog
- Mapping certain Neuwo keyword suggestions into choosen Hacklab Jkl taxonomy structure
  - Could re-use graphical yEd mapping method as in https://github.com/jasalt/robotag or something
- Finding way to utilise https://taxopress.com or other tag tools on Wordpress when creating blog content in the future