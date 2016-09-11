# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import requests

url = 'http://www.watchcount.com/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
r = requests.get(url, headers=headers)

print(str(r.status_code))

# r = requests.get('http://www.watchcount.com/completed.php?bkw=beatles+%28airbed%2C%22air+bed%22%2Clilo%2C%22li+lo%22%29&bcat=0&bcts=&sfsb=Show+Me%21&csbin=all&cssrt=ts&bslr=&bnp=&bxp=#serp')
# r = requests.get('http://www.watchcount.com/')
# r = requests.get('http://www.ebay.com/')

# print(str(r.status_code))
