from PIL import Image
from multiprocessing import Pool
import requests
import time
import os

url = "https://picsum.photos/2000/3000"
output_dir = './DAY5/output'

# Function to download an image
def download_image(index):
    # Make sure the directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        with open(f"{output_dir}/image_{index}.jpg", "wb") as file:
            file.write(response.content)
        print(f"Downloaded image_{index}.jpg")
 
# # Without multiprocessing (sequential download)
def download_images_sequential():  # Took 12.72 Second
    start_time = time.time()
    for i in range(2):
        download_image(i)
    end_time = time.time()
    print(f"Sequential download took: {end_time - start_time:.2f} seconds")

 
# # With multiprocessing (download)
def download_images_multiprocessing():
    start_time = time.time()
    p=Pool()
    l=[x for x in range(5)]
    p.map(download_image,l)
    # print(data)
    end_time = time.time()
    print(f"Multiprocessing download took: {end_time - start_time:.2f} seconds")


 
# # Run both functions to compare the execution times
def main():
    print("Starting sequential download...")
    download_images_sequential()
    
    print("\nStarting multiprocessing download...")
    download_images_multiprocessing()

if __name__=="__main__":
    main()