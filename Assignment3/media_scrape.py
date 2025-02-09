import aiohttp
import asyncio
from bs4 import BeautifulSoup
import logging
import json

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

async def fetch_data_from_article(session, url, title_tag, title_class, body_tag, body_class):
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

async def save_to_markdown(title, body, filename):
    """ Async function to save title and body in markdown file """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'# {title}\n\n{body}\n')
        print(f'File Saved successfully in {filename}')
    except Exception as e:
        logging.error(f'Error saving to {filename}: {e}')

async def scrape_media(site_name, config):
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
        title, body = await fetch_data_from_article(session, url, title_tag, title_class, body_tag, body_class)
        
        if title and body:
            filename = f"scrape_{site_name}.md"
            await save_to_markdown(title, body, filename)

async def main():
    # Load the config file
    config = load_config()
    
    if not config:
        print("Failed to load configuration.")
        return
    
    print('Enter Your Choice To Get The News Information:-')
    print("1. Indian Express\n2. The Hindu\n3. Both\n")
    
    choice = input("Enter your choice: ").strip()
    
    # Using async/await for simultaneous scraping
    match choice:
        case "1":
            # Scrape Indian Express asynchronously
            await scrape_media("IndianExpress", config)
        case "2":
            # Scrape The Hindu asynchronously
            await scrape_media("TheHindu", config)
        case"3":
            # Scrape both Indian Express and The Hindu asynchronously
            await asyncio.gather(
                scrape_media("IndianExpress", config),
                scrape_media("TheHindu", config)
            )
        case _:
            print("Invalid choice.")

if __name__ == '__main__':
    asyncio.run(main())
