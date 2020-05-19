# Importing selector
from scrapy import Selector

# Importing requests to load html data
import requests

# Creating a container for the url to scrap all the content of jumia home page
url = "https://www.jumia.com.ng"

# Creating a container to hold the HTML source
html = requests.get(url).content

# Creating a selector object
sel = Selector(text=html)

# Printing out the total elements in the page
print(len(sel.xpath("//*")))

# Selecting all Id in the home page
print(sel.xpath("//@id"))

# Searching for a particular class attribute
print(sel.xpath("//p[@class = '-mas -elli2']"))
