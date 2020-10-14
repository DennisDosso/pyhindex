import requests as rs
from lxml import html


url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=%22drugbank%22+%2B+%22DB00006%22&btnG="
page = rs.get(url)
print(page.content)
tree = html.fromstring(page.content)

#extract with an x-path the necessary elements
elements = tree.xpath('//div[@class="gs_ab_mdw"]/text()')
payload = elements[0]
parts = payload.split(" ")
citations = parts[1]
print(citations)