# Construct URL for search because the url are dynamic
def construct_url_for_search(search_content, search_engine, page):
    """
    Constructs a dynamic URL for a search query based on the search engine and page number.

    This function builds a URL to query the search engine for news results, with pagination support.

    Parameters:
    - search_content (str): The search query or term to look for.
    - search_engine (str): The search engine to use ('Google', 'Yahoo', or 'Bing').
    - page (int): The page number of results to fetch (0-based index).

    Returns:
    - str: The constructed URL for the search query on the specified search engine.
    """
    
    search_content = search_content.replace(' ', '+')
    base_urls = {
        'Google': f'https://news.google.com/search?q={search_content}',
        'Yahoo': f'https://news.search.yahoo.com/search?q={search_content}&b={page * 10}',
        'Bing': f'https://www.bing.com/news/search?q={search_content}&first={(page*10)+1}'
    }
    return base_urls.get(search_engine, '')