import requests as rs
from urllib.request import urlopen #to open an html page through a link
import json
from html.parser import HTMLParser #to parse html
from lxml import html
from bs4 import BeautifulSoup

import argparse

from googlesearch import search as gsearch

def news():
    """This methods returns error 401: unauthorized.
    That sucked, so I decided to use a different library"""
    #the url we want to open
    url = 'http://www.hindustantimes.com/top-news'
    #open with a GET method
    resp = rs.get(url)

    print(resp.status_code)

    #the response 200 means OK status
    if resp.status_code==200:
        print('Successfully opened the web page')

def news2():
    """this method works, yay! Now I can read a webpage. I need now to also parse it"""
    link = "https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python"
    f = urlopen(link)
    myfile = f.read()
    print(myfile)

def news3():
    """this presents yet another way to read a page. This time we are using the package properties
    Also, we are saving the page in an html tree, and using XPath to query it.
    THIS IS THE RIGHT SOLUTION (WO-HOO)
    """
    page = rs.get('http://econpy.pythonanywhere.com/ex/001.html')
    # print(page.content)
    tree = html.fromstring(page.content)
    #prepare an XPath query
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    print(buyers)


def parser_test_1():
    link = "https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python"
    f = urlopen(link)
    myfile = f.read() # now I have the file in the variable myfile in format byte
    file = str(myfile, 'utf-8') # convert byte to a nice string with utf-8 decoding
    parser = HTMLParser.feed(file)


def drug_bank_test_1():
    """ This method contains the XPath query necessary to parse my drug pages in Drugbank
    WO-HOO
    """
    #read the page
    page = rs.get('https://www.drugbank.ca/drugs?approved=1&c=name&d=up') # this is the first page of the drugs
    tree = html.fromstring(page.content)
    tests = tree.xpath('//td[@class="name-value text-sm-center drug-name"]/strong/a/@href') # this Xpath query returns
    #the h-ref of the links bringing me to drugs. In this way, I obtain the links to the drugs
    print(tests)

def ask_google_1():
    """this actually asks google but takes one url at the time"""
    #this is the base url, the url used for each page of drugbank
    base_url = 'https://www.drugbank.ca'
    #one example of substring to add to the base_url. It identifies one drug in the database
    addendum = '/drugs/DB11331'
    link = base_url + addendum
    #now we kindly ask google
    query = "link:" + link
    for j in gsearch(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)

def ask_google_1_1():
    """this actually asks google but takes one url at the time"""
    #this is the base url, the url used for each page of drugbank
    base_url = 'https://www.drugbank.ca'
    # base_url = 'www.drugbank.ca'
    #one example of substring to add to the base_url. It identifies one drug in the database
    link = base_url
    #now we kindly ask google
    query = "link:" + link
    counter = 0
    my_results_list = []
    for j in gsearch(query,
                     tld="com",
                     lang = "en",
                     num=10,
                     start = 0,
                     stop=None,
                     pause=2.0):
        counter+=1
        my_results_list.append(j)
        print('counter so far: ' + str(counter))
    print(counter)
    print(my_results_list)


def ask_google_2():
   """not working, Google obfuscates things"""
   page = rs.get('https://www.google.com/search?q=www.drugbank.ca')
   tree = html.fromstring(page.content)
   #now we get from this nice html page our results
   # solution = tree.xpath('//div[@id="result-stats"]')
   print(page.json)

def ask_google_json():
    data = urlopen('https://www.google.com/search?q=www.drugbank.ca')

def ask_bing():
    page = rs.get('https://www.bing.com/search?q=www.drugbank.ca')
    print(page.text)

# news() #done, it does not work
# news2() # done, it works
# news3() # done, it works and it is what I was looking for
# parser_test_1()

# drug_bank_test_1() #it works, thus we can scrap drugbank
# ask_google_1()
# ask_google_2()
# ask_google_json()
ask_google_1_1()