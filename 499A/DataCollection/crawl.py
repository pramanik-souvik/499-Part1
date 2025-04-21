import os
import requests
from bs4 import BeautifulSoup

def scrape_to_markdown(url, folder_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string.strip().replace(" ", "_") if soup.title else "untitled"
        content = soup.get_text()
        
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, f"{title}.md")
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# {soup.title.string.strip() if soup.title else 'Untitled'}\n\n")
            md_file.write(content)
        
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    url = input("Enter the URL to scrape: ").strip()
    folder_path = "markdown"
    
    scrape_to_markdown(url, folder_path)
