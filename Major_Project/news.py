import pandas as pd
import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

# Decorator function to calculate execution time
def execution_time(func):
    async def wrapper(*args,**kwargs):
        start_time=time.time()
        result=await func(*args,**kwargs)
        end_time=time.time()
        print(f'Execution time :{end_time-start_time}')
        return result
    return wrapper

# Load config files
def load_json():
    with open('./config.json', 'r') as file:
        data = json.load(file)
    return data


# This function takes a list of company names and keywords, and generates search queries by combining them
def generate_search_queries(companies, keywords):
    return [f'{company} {keyword}' for company in companies for keyword in keywords]


# Construct URL for search because the url are dynamic
def construct_url_for_search(search_content, search_engine, page):
    search_content = search_content.replace(' ', '+')
    base_urls = {
        'Google': f'https://news.google.com/search?q={search_content}&tbm=nws&start={page * 10}',
        'Yahoo': f'https://news.search.yahoo.com/search?q={search_content}&b={page * 10}',
        'Bing': f'https://www.bing.com/news/search?q={search_content}&first={page * 10}'
    }
    return base_urls.get(search_engine, '')


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


# Extract articles from the soup object when each search engine having different HTML structure
def extract_articles(soup, engine):
    article_lst = []
    if not soup:
        return article_lst
    if engine == "Google":
        articles = soup.find_all('article', {"class": "IFHyqb DeXSAc"})
        for article in articles[:10]:
            link_of_news = article.find('a', {'class': 'WwrzSb'})['href']
            title = article.find('a', {'class': 'JtKRv'}).text
            timestamp = article.find('time')
            data_time_value = timestamp['datetime']
            media_name = article.find('div', {'class': 'vr1PYe'}).text
            article_lst.append((link_of_news, title, data_time_value.split("T")[0], media_name))
    elif engine == "Yahoo":
        articles = soup.find_all('div', {"class": "dd NewsArticle"})
        for article in articles[:10]:
            title_ = article.find('h4', {'class': 's-title fz-20 lh-m fw-500 ls-027 mt-8 mb-2'})
            link_of_news = title_.find('a')['href']
            title = title_.find('a').text
            data_time_value = article.find('span', {'class': 's-time fz-14 lh-18 fc-dustygray fl-l mr-4'}).text
            media_name = article.find('span', {'class': 's-source fw-l'}).text
            article_lst.append((link_of_news, title, data_time_value, media_name))
    elif engine == 'Bing':
        articles = soup.find_all('div', {"class": "news-card newsitem cardcommon"})
        for article in articles[:10]:
            link_of_news = article.find('a', {'class': 'title'})['href']
            title = article.find('a', {'class': 'title'}).text
            data_time_value = article.find('span', {'aria-label': True}).text
            media_name_ = article.find('div', {'class': 'source set_top'})
            if media_name_:
                img_tag = media_name_.find('img')
                if img_tag and img_tag.has_attr('title'):
                    media_name = img_tag['title']
                else:
                    media_name = media_name_.text.strip()
            else:
                media_name = 'Unknown'
            article_lst.append((link_of_news, title, data_time_value, media_name))

    return article_lst



# Save the results to CSV using pandas DataFrame
def save_to_csv(data, file_name='news_results_2.csv'):
    df = pd.DataFrame(data, columns=["search_content", "search_engine",  "link_of_news", "title", "timestamp", "media_name"])
    df.to_csv(file_name, index=False, encoding='utf-8')
    print(f'Data successfully saved in {file_name}')







# Main async function to run everything
@execution_time
async def main():
    config = load_json()
    search_queries = generate_search_queries(config['company_names'], config['keywords'])
    search_engines = config['Search_engine']
    num_pages = config['Number_of_Pages']


    # Gather results concurrently for all search queries and pages
    results = await fetch_all_results(search_queries, search_engines, num_pages)

    # Save the results to CSV
    save_to_csv(results)


# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())

