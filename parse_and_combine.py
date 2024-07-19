import requests
from bs4 import BeautifulSoup
import os

# URLs to fetch
url1 = "https://github.com/PME-Crew/app-ads.txt/blob/master/app-ads.txt"
url2 = "https://cas.ai/app-ads.txt"

def fetch_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

def combine_texts(text1, text2):
    return text1 + "\n\n" + text2

def main():
    text1 = fetch_text(url1)
    text2 = fetch_text(url2)
    combined_text = combine_texts(text1, text2)

    output_file = "app-ads.txt"
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            existing_text = file.read()
    else:
        existing_text = ""

    if combined_text != existing_text:
        with open(output_file, 'w') as file:
            file.write(combined_text)
        print("Changes detected and file updated.")
        return True
    else:
        print("No changes detected.")
        return False

if __name__ == "__main__":
    if main():
        exit(0)
    else:
        exit(1)
