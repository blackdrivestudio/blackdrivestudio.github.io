import os
import requests

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    with open(filename, 'w') as file:
        file.write(response.text)

def main():
    script_url1 = os.getenv('SCRIPT_URL1')
    script_url2 = os.getenv('SCRIPT_URL2')

    if not script_url1 or not script_url2:
        print("SCRIPT_URL1 or SCRIPT_URL2 environment variable is not set.")
        return

    # Download the files
    download_file(script_url1, 'parse_and_combine.py')
    download_file(script_url2, 'parse_app_ads_daily.yml')

if __name__ == "__main__":
    main()
