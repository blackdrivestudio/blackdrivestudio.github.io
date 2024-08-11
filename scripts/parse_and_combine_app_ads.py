import requests
from bs4 import BeautifulSoup
import os

def fetch_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

def combine_texts(texts):
    return "#\n".join(texts)

def main():
    urls = []
    index = 1
    while True:
        url = os.getenv(f'APP_ADS_URL{index}')
        if not url:
            break
        urls.append(url)
        index += 1
    
    if not urls:
        print("No URLs are set properly.")
        return
    
    texts = [fetch_text(url) for url in urls]
    combined_text = combine_texts(texts)

    output_file = "app-ads.txt"
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            existing_text = file.read()
    else:
        existing_text = ""

    changes_detected = "false"
    if combined_text != existing_text:
        with open(output_file, 'w') as file:
            file.write(combined_text)
        changes_detected = "true"

    print(f"::set-output name=changes_detected::{changes_detected}")

if name == "main":
    main()
