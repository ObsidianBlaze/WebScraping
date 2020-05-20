# Importing the scraping modules
from scrapy import Selector
import requests

# The url to the scraped site
url = "https://www.datacamp.com/courses/all"

# Loading the content of the url
html = requests.get(url).content

# Creating an object of the selector class
sel = Selector(text=html)

# Searching with css selector to return an empty value
print(sel.css('p.-mvs::text').extract())

#  Printing out the total number of tags in the home page
print(len(sel.css('html *')))

# Printing out all the courses offered in the home page
# all_courses = sel.css('h3.course-block__title::text').extract()
# Extracting the text
# all_courses_text = all_courses.css(' ::text').extract()
# Printing out the courses
# print(all_courses)

print(sel.css('div.course-block > a::attr(href)').extract())