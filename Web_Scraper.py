"""
 This small project is about webscraping
 And parsing XML sitemaps
 
"""
# Loading packages -for example urllib to fetch XML sitemaps
import pandas as pd
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
  
# url goes to the XML sitemap
# BeautifulSoup lxml allows you to parse XML files
def retrieve_sitemap(url):
      resp = urllib.request.urlopen(url)
      xml = BeautifulSoup(resp, 'lxml-xml', from_encoding=resp.info().get_param('charset'))
      return xml
      
# Finding sitemap at the root(sitemap.xml) or using robots.txt      
url = "https://dreamsfertilityclinic.com/page-sitemap.xml"
xml = retrieve_sitemap(url)
    
print(xml)    
