import asyncio
from scraper.config_manager import load_json
from scraper.fetcher import fetch_all_results
from scraper.file_manager import save_to_csv
from scraper.search_query import generate_search_queries
from utils.execution_time import execution_time

@execution_time
async def main():
    config = load_json() # load json file
    search_queries = generate_search_queries(config['company_names'], config['keywords'])
    search_engines = config['Search_engine']
    num_pages = config['Number_of_Pages']

    # Gather results concurrently for all search queries and pages
    results = await fetch_all_results(search_queries, search_engines, num_pages)
    

    # Save the results to CSV
    save_to_csv(results)


if __name__ == "__main__":
    asyncio.run(main())
