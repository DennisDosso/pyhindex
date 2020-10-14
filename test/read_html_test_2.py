import requests as rs
from lxml import html

#I needed another clean file where to test how to read html

#get the html from this webpage
page = rs.get('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=%22drugbank%22+%2B+%22DB00001%22&btnG=')
#page.content is the html content of this page
print(page.content)

#prepare a tree representation of the page
tree = html.fromstring(page.content)

#prepare an Xpath query

citations = tree.xpath('//div[@class="gs_ab_mdw"]/text()')
print(citations)

