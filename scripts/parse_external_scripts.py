import os
import requests

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    with open(filename, 'w') as file:
        file.write(response.text)

def main():
    script_url1 = os.getenv('SCRIPT_URL_1')
    script_url2 = os.getenv('SCRIPT_URL_2')

    if not script_url1 or not script_url2:
        print("Some SCRIPT_URL environment variable is not set.")
        return

    # Download the files
    download_file(script_url1, 'parse_app_ads_daily.yml')
    download_file(script_url2, 'parse_and_combine_app_ads.py')

if __name__ == "__main__":
    main()
