import scrapy
import json
import os
import sys
import requests
import requests as req
from bs4 import BeautifulSoup



#print h1 tags in the page zoesquad.me
#class ZoesquadSpider(scrapy.Spider):
# name = "zoesquad"
# allowed_domains = ["zoesquad.me"]
# start_urls = [
#      "https://zoesquad.me/",
#  ]

#  def parse(self, response):
#     for h1 in response.css('h1'):
#       yield {
#            'h1': h1.css('::text').extract_first(),
#      }


# Python program to print all heading tags
import requests
from bs4 import BeautifulSoup

# scraping a wikipedia article
url_link = 'https://zoesquad.me/'
request = requests.get(url_link)

Soup = BeautifulSoup(request.text, 'lxml')

# creating a list of all common heading tags
heading_tags = ["h1", "h2", "h3"]
for tags in Soup.find_all(heading_tags):
    print(tags.name + ' -> ' + tags.text.strip())

