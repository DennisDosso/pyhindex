import requests as rs
from lxml import html
from pyhindex.properties.urls import drugbank_drugs
from pyhindex.properties.paths import drugs_id_output_path


# initialize the url string to query drugbank
url = drugbank_drugs % 1

#open the output file
f = open(drugs_id_output_path, "w")

# # get the page
# page = rs.get(url)
page = rs.get("https://go.drugbank.com/drugs?approved=1&c=name&d=up")
# print(page.content)

#prepare a tree representation of the page
tree = html.fromstring(page.content)

#extract the urls of the drugs
elements = tree.xpath('//tbody/tr/td[@class="name-value text-sm-center drug-name"]//a/@href')
# print(elements)

for s in elements :
    parts = s.split("/")
    # print(parts)
    id = parts[2]
    f.write(id + "\n")
    print(id)

f.close()





