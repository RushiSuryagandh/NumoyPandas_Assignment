import aiohttp
import requests
import asyncio
from bs4 import BeautifulSoup
import logging

# Create and configure logger
logging.basicConfig(filename="./scraping.log",
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    filemode='w',
                    level=logging.INFO)


def fetch_data_from_article(url,title_tag,title_class,body_tag,body_class):
    """
    Common function to fetch the data for two functions.
    Get the url and tags data and using this call requests to get the data.
    Fetch the data by using variables passing it to the function.

    Args:
        url (string): perticular news url
        title_tag : tag name of title
        title_class : class name title_tag
        body_tag: tag name of information stored in body tag
        body_class : class name of body_tag

    Returns:
        text: returns title and body 
    """
    try:
        response=requests.get(url)
        soup=BeautifulSoup(response.content,'html.parser')
        # print(soup.prettify())
        title=soup.find(title_tag,class_=title_class).text.strip()
        body=soup.find(body_tag,class_=body_class)
        body_content=body.find_all('p')
        body=''
        for content in body_content:
            body+=content.text.strip()
            # print(content.text)
            logging.info("Successfull")
        return title,body
    except Exception as e:
        logging.error(f'Error fetching article from {url}:{e}')
        return None,None
    


def save_to_markdown(title,body,filename):
    """To save title and body in markdown file

    Args:
        title :Title name
        body : Text of news
        filename: file name which saved data
    """
    
    try:
        with open(filename,'w',encoding='utf-8')as file:
            file.write(f'# {title}\n\n{body}\n')
        print(f'File Saved successfully in {filename}')
    except Exception as e:
        logging.error(f'Error saving to {filename}:{e}')
    

def scrape_media_channel_1():
    """ function for media 'IndianExpress' 
        stored the class and tags 
        call fetch_data_from_article by passing the tags information
        fetch title and body and save it to markdown file
    """
    url='https://indianexpress.com/article/india/working-on-law-for-safe-migration-mea-to-panel-9819904/?ref=breaking_hp'
    title_tag='h1'
    title_class='native_story_title'
    body_tag='div'
    body_class='story_details'
    title,body=fetch_data_from_article(url,title_tag,title_class,body_tag,body_class)

    if title and body:
        save_to_markdown(title,body,'scrape_channel_1.md')
    
 
   
def scrape_media_channel_2():
    """ function for media 'The Hindu' 
        stored the class and tags 
        call fetch_data_from_article by passing the tags information
        fetch title and body and save it to markdown file
    """
    url='https://www.thehindu.com/news/international/bangladesh-has-become-a-land-of-terrorists-and-fighters-says-sheikh-hasina-after-demolition-of-residence-of-sheikh-mujibur-rahman/article69187048.ece'
    title_tag='h1'
    title_class='title'
    body_tag='div'
    body_class='col-xl-9 col-lg-8 col-md-12 col-sm-12 col-12 storyline'
    title,body=fetch_data_from_article(url,title_tag,title_class,body_tag,body_class)
    # print(title,body)
    if title and body:
        save_to_markdown(title,body,'scrape_channel_2.md')
    
    


def main():
    scrape_media_channel_1()
    scrape_media_channel_2()

if __name__=='__main__':
    main()

