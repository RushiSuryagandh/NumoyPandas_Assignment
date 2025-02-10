from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import fitz
import os
import re
import pandas as pd
from decorator import execution_time


def load_json():
    with open('./config2.json','r') as file:
        data= json.load(file)
        return data

def downlod_pdf(urls_data,download_dir):
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('prefs',{
        'download.default_directory':'C:\\Users\\RushikeshSuryagandh\\npAssignment\\Major_Project',  # Gives the directory path to store the pdf
        'download.prompt_for_download':False, # s/w doesn't ask user about confirmation of downloading 
        'plugins.always_open_pdf_externally':True # means that PDF files will always be opened in an external PDF viewer instead of within the software or browser itself.

    })
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    # This part uses a library called webdriver-manager to automatically download and manage the correct version of ChromeDriver (the Chrome browser’s WebDriver). don't have to manually download or specify the driver’s location.
    
    for url in urls_data: # for each url in urls_data
        # Extract the filename from the URL (or create a unique filename based on URL)
        file_name = url.split('/')[-1]
        file_path = os.path.join(download_dir, file_name)

        # Check if the file already exists
        if not os.path.exists(file_path):
            # If the file doesn't exist, download it
            driver.get(url)
            print(f"Downloading {file_name}...")
        else:
            # If the file exists, skip downloading
            print(f"{file_name} already exists. Skipping download.")
    
    driver.quit()


def fetch_pdf_files(directory_path):
    pdf_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check if the file ends with ".pdf"
            if file.endswith('.pdf'):
                # Append the full file path to the list
                pdf_files.append(os.path.join(root, file))
                
    # print(f"Found PDF: {pdf_files}") 
    return pdf_files




def extract_data_from_pdf(pdf_file_paths):
    text=''
    # print(pdf_file_paths)
    for pdf in pdf_file_paths:
        # print(pdf)
        open_pdf=fitz.open(pdf)
        time.sleep(2)

        # print(open_pdf)
        for page_num in range(4):
            text+=open_pdf[page_num].get_text('text')
        # time.sleep(2)
        # print(text)
    return text

def extract_data_from_regx(text):
    email_pattern=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}'
    cin_number_pattern=r'[A-Z]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}'
    mobile_number_pattern=r'\b(?:\d{3,5}[\s-]?)?[\d]{7,10}\b'
    pan_number_pattern=r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b'
    dates_pattern=r'\b\d{2}/\d{2}/\d{4}\b'
    website_pattern=r'\bhttps?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b|\bwww\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
    
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
    time.sleep(2)
    return data



def save_to_csv(data, file_name='pdf_results.csv'):
    df = pd.DataFrame(data, columns=["Email", "CIN",  "Mobile_Number", "PAN", "Date", "Website"])
    df.to_csv(file_name, index=False, encoding='utf-8')
    print(f'Data successfully saved in {file_name}')

    

    
@execution_time
def main():
    config =load_json()
    urls_data = config['urls']
    download_dir=config['directory_path']
    downlod_pdf(urls_data,download_dir)
    time.sleep(1)
    directory_path = config['directory_path']
    #  Fetch the PDF file paths
    pdf_file_paths = fetch_pdf_files(directory_path)

    # Extract data from PDFs
    text = extract_data_from_pdf(pdf_file_paths)
    # Extract data using regex
    data = extract_data_from_regx(text)
    # Save to CSV
    save_to_csv(data)

    
    
if __name__=="__main__":
    main()
    
    
    

    
    
    
