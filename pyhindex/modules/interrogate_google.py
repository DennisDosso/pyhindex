import requests as rs
from lxml import html


def interrogate_google_scholar_to_get_number_of_citations(url_query : str) :
    """ Given a query url, returns the number of citing elements to the result, i.e. 
     the string "About x results" at the top of the page (it returns the x value)
     
     :return a string representing the number of citations corresponding to the queries element
     """
    #open the page
    page = rs.get(url_query)
    #also get the content of the page
    c = str(page.content)

    if "Why did this happen?" in c:
        #we reached the end of our permissions to access to the google pages for today
        return "-1"

    tree = html.fromstring(page.content)

    elements = tree.xpath('//div[@class="gs_ab_mdw"]/text()')

    if len(elements) == 0 :
        # this elements received no citations
        return "0"

    payload = elements[0]
    parts = payload.split(" ")
    if len(parts) == 3 :
        citations = parts[0]
    else :
        citations = parts[1]
    return citations