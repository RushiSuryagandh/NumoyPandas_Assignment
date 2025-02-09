import requests
from bs4 import BeautifulSoup
import logging
import json
import threading
import time
import asyncio
import aiohttp
from multiprocessing import Process

# Create and configure logger
logging.basicConfig(filename="./scraping.log",
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    filemode='w',
                    level=logging.INFO)

# Function to load config from json file
def load_config(filename="config.json"):
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
        return config
    except Exception as e:
        logging.error(f"Error loading config file: {e}")
        return None

def fetch_data_from_article(url, title_tag, title_class, body_tag, body_class):
    """ Common function to fetch the data for two functions. """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find(title_tag, class_=title_class).text.strip()
        body = soup.find(body_tag, class_=body_class)
        body_content = body.find_all('p')
        
        body_text = ''
        for content in body_content:
            body_text += content.text.strip()
        
        logging.info("Successfully fetched article.")
        return title, body_text
    except Exception as e:
        logging.error(f'Error fetching article from {url}: {e}')
        return None, None

def save_to_markdown(title, body, filename):
    """ To save title and body in markdown file """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'# {title}\n\n{body}\n')
        print(f'File Saved successfully in {filename}')
    except Exception as e:
        logging.error(f'Error saving to {filename}: {e}')

def scrape_media(site_name, config):
    """ Function for scraping based on the site configuration """
    if site_name not in config:
        logging.error(f"Site configuration for {site_name} not found.")
        return
    
    site_config = config[site_name]
    
    url = site_config['url']
    title_tag = site_config['title_tag']
    title_class = site_config['title_class']
    body_tag = site_config['body_tag']
    body_class = site_config['body_class']
    
    title, body = fetch_data_from_article(url, title_tag, title_class, body_tag, body_class)
    
    if title and body:
        filename = f"scrape_{site_name}.md"
        save_to_markdown(title, body, filename)

# ---------- MULTITHREADING ----------

def scrape_media_threaded(site_name, config):
    """ Function for scraping using threading """
    scrape_media(site_name, config)

def multithreading_scrape(config):
    """ Use multithreading to scrape both websites at once """
    start_time = time.time()
    
    thread1 = threading.Thread(target=scrape_media_threaded, args=("IndianExpress", config))
    thread2 = threading.Thread(target=scrape_media_threaded, args=("TheHindu", config))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    end_time = time.time()
    print(f"Multithreading execution time: {end_time - start_time} seconds")

# ---------- MULTIPROCESSING ----------

def scrape_media_multiprocess(site_name, config):
    """ Function for scraping using multiprocessing """
    scrape_media(site_name, config)

def multiprocessing_scrape(config):
    """ Use multiprocessing to scrape both websites at once """
    start_time = time.time()
    
    process1 = Process(target=scrape_media_multiprocess, args=("IndianExpress", config))
    process2 = Process(target=scrape_media_multiprocess, args=("TheHindu", config))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time} seconds")

# ---------- ASYNC/AWAIT ----------

async def fetch_data_from_article_async(session, url, title_tag, title_class, body_tag, body_class):
    """ Async function to fetch the data for two functions. """
    try:
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            
            title = soup.find(title_tag, class_=title_class).text.strip()
            body = soup.find(body_tag, class_=body_class)
            body_content = body.find_all('p')
            
            body_text = ''
            for content in body_content:
                body_text += content.text.strip()
            
            logging.info("Successfully fetched article.")
            return title, body_text
    except Exception as e:
        logging.error(f'Error fetching article from {url}: {e}')
        return None, None

async def save_to_markdown_async(title, body, filename):
    """ Async function to save title and body in markdown file """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'# {title}\n\n{body}\n')
        print(f'File Saved successfully in {filename}')
    except Exception as e:
        logging.error(f'Error saving to {filename}: {e}')

async def scrape_media_async(site_name, config):
    """ Async function for scraping based on the site configuration """
    if site_name not in config:
        logging.error(f"Site configuration for {site_name} not found.")
        return
    
    site_config = config[site_name]
    
    url = site_config['url']
    title_tag = site_config['title_tag']
    title_class = site_config['title_class']
    body_tag = site_config['body_tag']
    body_class = site_config['body_class']
    
    async with aiohttp.ClientSession() as session:
        title, body = await fetch_data_from_article_async(session, url, title_tag, title_class, body_tag, body_class)
        
        if title and body:
            filename = f"scrape_{site_name}.md"
            await save_to_markdown_async(title, body, filename)

async def async_scrape(config):
    """ Use async/await to scrape both websites at once """
    start_time = time.time()
    
    await asyncio.gather(
        scrape_media_async("IndianExpress", config),
        scrape_media_async("TheHindu", config)
    )
    
    end_time = time.time()
    print(f"Async/Await execution time: {end_time - start_time:.4f} seconds")

# ---------- MAIN EXECUTION ----------

def main():
    # Load the config file
    config = load_config()
    
    if not config:
        print("Failed to load configuration.")
        return
    
    # Run each approach and measure execution time
    print("\nStarting Multithreading...\n")
    multithreading_scrape(config)
    
    print("\nStarting Multiprocessing...\n")
    multiprocessing_scrape(config)
    
    print("\nStarting Async/Await...\n")
    asyncio.run(async_scrape(config))

if __name__ == '__main__':
    main()
