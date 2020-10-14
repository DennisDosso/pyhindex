#a string to get drugbank pages that contain drugs
drugbank_drugs = 'https://go.drugbank.com/drugs?approved=%i&c=name&d=up'

# a url of a generic drug page (the above url is wrong)
drugbank_drug_url = "https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=%i"

drugbank_target_url = "https://go.drugbank.com/targets?page=%i"

google_scholar_query_url_drugbank = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=%22drugbank%22+%2B+%22!!replace_here%22&btnG="