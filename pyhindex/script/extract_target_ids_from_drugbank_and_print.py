from pyhindex.modules.extract_ids_from_drugbank_page import extract_ids_from_target_drugbank_page
from pyhindex.properties.urls import drugbank_target_url
from pyhindex.properties.paths import target_id_output_path

#set containing our ids
set_of_ids = set()
# output file where we write the ids
f = open(target_id_output_path, "w")

for i in range(1, 929) :
    #as of now, there is a total of 928 target pages in drugbank

    #prepare one url, corresponding to one page of drugs (the page contains the list of drugs)
    url = drugbank_target_url % i
    set_of_ids_of_this_page = extract_ids_from_target_drugbank_page(url)
    #merge the two sets
    set_of_ids.update(set_of_ids_of_this_page)
    print("done page " + str(i) + " of 928")


print("now printing")
#print the ids
for id_ in set_of_ids:
    f.write(id_ + "\n")

f.close()



