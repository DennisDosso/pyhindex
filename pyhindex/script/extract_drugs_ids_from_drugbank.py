from pyhindex.modules.extract_ids_from_drugbank_page import extract_ids_from_drugbank_page
from pyhindex.properties.urls import drugbank_drug_url
from pyhindex.properties.paths import drugs_id_output_path

#list containing our ids
ids_of_this_pageid_list = []

# output file where we write the ids
f = open(drugs_id_output_path, "w")

for i in range(1, 107) :
    #as of now, there is a total of 106 drug pages in drugbank

    #prepare one url, corresponding to one page of drugs (the page contains the list of drugs)
    url = drugbank_drug_url % i
    ids_of_this_page = extract_ids_from_drugbank_page(url)
    #print the ids
    for id_ in ids_of_this_page:
        f.write(id_ + "\n")

    print("done page " + str(i) + "of 107")



f.close()



