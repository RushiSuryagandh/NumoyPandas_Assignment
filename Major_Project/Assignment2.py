import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
import time
import fitz
import os
import re
import csv
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

def load_json():
    with open('./config2.json','r')as file:
        data=json.load(file)
    return data

async def download_pdf(url,options,session):
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    async with session.get(url)as response:
        if response.status==200:
            driver.get(url)
            driver.implicitly_wait(2)
        driver.quit()


async def downlod_pdfs(urls_data):
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('prefs',{
        'download.default_directory':'C:\\Users\\RushikeshSuryagandh\\npAssignment\\Major_Project',  # Gives the directory path to store the pdf
        'download.prompt_for_download':False, # s/w doesn't ask user about confirmation of downloading 
        'plugins.always_open_pdf_externally':True # means that PDF files will always be opened in an external PDF viewer instead of within the software or browser itself.

    })
    

    async with aiohttp.ClientSession() as session:
        tasks=[download_pdf(url,options,session) for url in urls_data]
        await asyncio.gather(*tasks)
    


def fetch_pdf_files(directory_path):
    pdf_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check if the file ends with ".pdf"
            if file.endswith('.pdf'):
                # Append the full file path to the list
                pdf_files.append(os.path.join(root, file))
    
    return pdf_files




def extract_data_from_pdf(pdf_file_path):
    open_pdf=fitz.open(pdf_file_path)
    text=""
    for page_num in range(3):
        text+=open_pdf[page_num].get_text('text')
    return text

def extract_data_from_regx(text):
    email_pattern=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}'
    cin_number_pattern=r'[A-Z]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}'
    mobile_number_pattern=r'\b(?:\d{3,5}[\s-]?)?[\d]{7,10}\b'
    pan_number_pattern=r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b'
    dates_pattern=r'\b\d{2}/\d{2}/\d{4}\b'
    website_pattern=r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    emails = re.findall(email_pattern, text)
    cin_numbers = re.findall(cin_number_pattern, text)
    mobile_numbers = re.findall(mobile_number_pattern, text)
    pan_numbers = re.findall(pan_number_pattern, text)
    dates = re.findall(dates_pattern, text)
    websites = re.findall(website_pattern, text)

    # print(emails,cin_numbers,mobile_numbers,pan_numbers,dates,websites)
    data = []
    for i in range(max(len(emails), len(cin_numbers), len(mobile_numbers), len(pan_numbers), len(dates), len(websites))):
        data_row = {
            'Email': emails[i] if i < len(emails) else '',
            'CIN': cin_numbers[i] if i < len(cin_numbers) else '',
            'Mobile Number': mobile_numbers[i] if i < len(mobile_numbers) else '',
            'PAN': pan_numbers[i] if i < len(pan_numbers) else '',
            'Date': dates[i] if i < len(dates) else '',
            'Website': websites[i] if i < len(websites) else ''
        }
        data.append(data_row)
    return data

def save_to_csv(data,file_name='pdf_results.csv') :
    with open(file_name,mode='w',newline='',encoding='utf-8')as file:
        writer = csv.DictWriter(file, fieldnames=['Email', 'CIN', 'Mobile Number', 'PAN', 'Date', 'Website'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f'Data Succesfully saved in {file_name}')

    
async def process_pdf(pdf_file_path):
    text=extract_data_from_pdf(pdf_file_path)
    return extract_data_from_regx(text)
    

async def main():
    config=load_json()
    urls_data=config['urls']
    await downlod_pdfs(urls_data)
   
    # Specify your directory path
    directory_path = config['directory_path']

    # Fetch the PDF file paths
    pdf_file_paths = fetch_pdf_files(directory_path)
    with ThreadPoolExecutor() as executor:
        tasks=[process_pdf(pdf_file_path) for pdf_file_path in pdf_file_paths]
        results=await asyncio.gather(*tasks)
    data=[item for sublist in results for item in sublist]
    
    save_to_csv(data)
    
    
if __name__=="__main__":
    start_time=time.time()
    asyncio.run(main())
    end_time=time.time()
    print(end_time-start_time)
    
    
    
