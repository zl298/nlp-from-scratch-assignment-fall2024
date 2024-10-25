#This is the code file for scarping the data from different website
import requests
from bs4 import BeautifulSoup

#input the web page
main_url = 'https://en.wikipedia.org/wiki/The_Andy_Warhol_Museum'

response = requests.get(main_url)

#solve the 403 issues

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive'
}

# Send the request with headers
response = requests.get(main_url, headers=headers)

with open('The Andy Warhol Museum_wiki.txt', 'w', encoding='utf-8') as file:

    if response.status_code == 200:
        # Parse the main page content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Scrape the main page content
        main_content = soup.get_text(separator="\n", strip=True)
        
        # Write the main page content to the file
        file.write(f"Main Page Content:\n{main_content}\n")
        file.write("-" * 50 + "\n")  # Separator between pages
        
        # Find links to the subpages (about, schedule, etc.)
        subpage_links = soup.find_all('a', href=True, text=True)  # Adjust based on the actual structure

        for link in subpage_links:
            subpage_name = link.text.strip()  # Get the subpage name (e.g., "about", "schedule")
            subpage_url = link['href']        # Get the subpage URL

            if subpage_url.startswith('tel:'):
                    continue

            if subpage_url.startswith('webcal:'):
                    continue


            # Check if the URL is relative or absolute and make it absolute if necessary
            if not subpage_url.startswith('http'):
                subpage_url = requests.compat.urljoin(main_url, subpage_url)
            
            # Send a new request to the subpage
            subpage_response = requests.get(subpage_url, headers=headers)

            if subpage_response.status_code == 200:
                # Parse the subpage content
                subpage_soup = BeautifulSoup(subpage_response.content, 'html.parser')
                
                # Extract text content from the subpage
                subpage_content = subpage_soup.get_text(separator="\n", strip=True)
                
                # Write the subpage name and content to the file
                file.write(f"Subpage: {subpage_name} ({subpage_url})\n")
                file.write(f"Subpage Content:\n{subpage_content}\n")
                file.write("-" * 50 + "\n")  # Separator between pages
            else:
                file.write(f"Failed to retrieve subpage {subpage_name}. Status code: {subpage_response.status_code}\n")
                file.write("-" * 50 + "\n")
    else:
        file.write(f"Failed to retrieve the main page. Status code: {response.status_code}\n")