import requests as rs
from lxml import html

def extract_ids_from_drugbank_page (page_url : str) :
    """ interrogates a drugbank webpage and extracts, through the use of an xpath query,
    all the IDS of drugs in that page. If it does not work, it may be that the xpath query is no
     longer valid

     @:return a list of ids"""
    #the list of our elements
    list = []

    #open the url page
    page = rs.get(page_url)
    #prepare the page as a html tree
    tree = html.fromstring(page.content)

    # extract the urls of the drugs
    elements = tree.xpath('//tbody/tr/td[@class="name-value text-sm-center drug-name"]//a/@href')

    for s in elements:
        parts = s.split("/")
        # print(parts)
        id = parts[2]
        list.append(id)

    return list


def extract_ids_from_target_drugbank_page(page_url: str) :
    string_set = set()

    # open the url page
    page = rs.get(page_url)
    # prepare the page as a html tree
    tree = html.fromstring(page.content)

    # extract the urls of the drugs
    elements = tree.xpath('//tbody/tr/td/a[@target="_blank"]/@href')

    for s in elements:
        parts = s.split("/")
        # print(parts)
        id = parts[2]
        string_set.add(id)

    return string_set
