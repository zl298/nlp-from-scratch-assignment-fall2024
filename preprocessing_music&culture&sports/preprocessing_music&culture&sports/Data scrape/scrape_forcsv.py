import requests
from bs4 import BeautifulSoup

# List of multiple main page URLs
main_urls = [
    'https://www.pittsburghsymphony.org/pso_home/web/community-landing/learning-programs/student-side-by-side-program',
    'https://pittsburghsymphony.org/pso_home/web/community-landing/learning-and-engagement-volunteer-corps',
    'https://www.pittsburghsymphony.org/pso_home/web/community-landing/learning-programs/schooltime-programs',
    'https://www.pittsburghsymphony.org/pso_home/web/community-landing/learning-programs/schooltime-concerts',
    'https://www.pittsburghsymphony.org/pso_home/web/community-landing/learning-programs/schooltime-concerts/digital-schooltime'

]


# Add headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Open the file in write mode to save the scraped content
with open('Symphony_main.txt', 'w', encoding='utf-8') as file:

    # Loop through each main URL
    for main_url in main_urls:
        # Send the request to the main page
        response = requests.get(main_url, headers=headers)

        if response.status_code == 200:
            # Parse the main page content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Scrape the main page content
            main_content = soup.get_text(separator="\n", strip=True)
            
            # Write the main page content to the file
            file.write(f"Main Page URL: {main_url}\n")
            file.write(f"Main Page Content:\n{main_content}\n")
            file.write("-" * 50 + "\n")  # Separator between pages
            
            
        else:
            file.write(f"Failed to retrieve the main page at {main_url}. Status code: {response.status_code}\n")
            file.write("-" * 50 + "\n")