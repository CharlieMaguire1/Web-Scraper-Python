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

#Find out what type of sitemap - sitemapindex or urlset
def retrieve_sitemap_type(xml):
    sitemap_index = xml.find_all('sitemapindex')
    sitemap_urlset = xml.find_all('urlset')
    if sitemap_index:
        return 'This sitemap is a sitemapindex'
    elif sitemap_urlset:
        return 'This sitemap is an urlset'
    else:
        return

#Call out the function to find the type of sitemap
type_of_sitemap = retrieve_sitemap_type(xml)
print(type_of_sitemap)

