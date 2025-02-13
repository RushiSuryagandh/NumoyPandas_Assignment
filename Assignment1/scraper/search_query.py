# This function takes a list of company names and keywords, and generates search queries by combining them
def generate_search_queries(companies, keywords):
    return [f'{company} {keyword}' for company in companies for keyword in keywords]