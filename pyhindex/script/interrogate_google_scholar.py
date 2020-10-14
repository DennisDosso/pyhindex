from pyhindex.properties.paths import drugs_id_output_path as drug_path

from pyhindex.properties.urls import google_scholar_query_url_drugbank as scholar_url
from pyhindex.properties.paths import output_drugs_citations as output_path

from pyhindex.modules.interrogate_google import interrogate_google_scholar_to_get_number_of_citations

# open the file containing the ids of the drugs
f = open(drug_path, "r")
# csv file where we write the answers. Each line is in the form id_of_the_drug_or_target, number_of_citations
output_f = open(output_path, "w")

#a counter I used during debug
counter = 0
for line in f :
    line = line.replace("\n", "") #remove the \n, for some reason I left it there

    #now prepare the url for the interrogation
    # I had to use this awful trick to substitute the wildcard here, probably due to the nature of the url
    query_url = scholar_url.replace("!!replace_here", line)
    citations = interrogate_google_scholar_to_get_number_of_citations(query_url)

    if citations == "-1":
        #need to stop
        print("ended the allowed queries on Google for today! Finished at the id: " + line)
        break

    output_f.write(line + "," + citations + "\n")
    counter += 1

    if(counter % 10 == 0) :
        print("covered " + str(counter) + " elements")


f.close()
output_f.close()
