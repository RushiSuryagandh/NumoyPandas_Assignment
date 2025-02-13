import aiohttp
import asyncio
from bs4 import BeautifulSoup
from .url_constructor import construct_url_for_search
from .article_extractor import extract_articles

# Fetch search results asynchronously(Simultaneosly)
async def fetch_search_result(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, timeout=5) as response:
            if response.status == 200:
                return await response.text()
            else:
                return None
            
# It generates a list of URLs to fetch and then uses asyncio.gather() to run all fetch tasks concurrently.
async def fetch_all_results(search_queries, search_engines, num_pages):
    """
    Asynchronously fetches search results from multiple search engines and extracts article data.

    This function generates URLs for each search query and engine, fetches the HTML content for 
    each URL concurrently, and then extracts article details (link, title, timestamp, media name).

    Parameters:
    - search_queries (list of str): List of search terms to query.
    - search_engines (list of str): List of search engines to use (e.g., "Google", "Yahoo", "Bing").
    - num_pages (int): The number of result pages to fetch for each search query and engine.

    Returns:
    - list of lists: Each inner list contains [search_query, search_engine, link_of_news, title, timestamp, media_name].
    """
    results = []

    tasks = []  # List to store the asynchronous tasks

    # Generate all URLs to fetch
    for search_content in search_queries:
        for search_engine in search_engines:
            for page in range(num_pages):
                url = construct_url_for_search(search_content, search_engine, page)

                tasks.append(fetch_search_result(url))  # Append each fetch task(Couroutine Object)
   

    # Execute all requests concurrently
    html_responses = await asyncio.gather(*tasks)  # Gather all responses concurrently
    

    # Extract articles for each response
    result_index = 0  # Index to map HTML responses back to queries

    for search_content in search_queries:
        for search_engine in search_engines:
            for page in range(num_pages):
                html = html_responses[result_index]
                result_index += 1  # Move to the next HTML response
                soup = BeautifulSoup(html, 'html.parser') if html else None
                articles = extract_articles(soup, search_engine)
                for link_of_news, title, data_time_value, media_name in articles:
                    results.append([search_content, search_engine, link_of_news, title, data_time_value, media_name])

    return results