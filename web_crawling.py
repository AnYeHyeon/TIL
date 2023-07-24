from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("http://news.naver.com/")
bsObject = BeautifulSoup(html, "html.parser")

links_data = []
for link in bsObject.find_all('a'):  # Corrected 'fineall' to 'find_all'
    title = link.text.strip()
    url = link.get('href')
    if url and title:  # Only add links with non-empty titles and URLs
        links_data.append((title, url))

# Convert the list of tuples to a DataFrame
df = pd.DataFrame(links_data, columns=['Title', 'URL'])

# Save the DataFrame to an Excel file
file_name = "crawler_links.xlsx"
df.to_excel(file_name, index=False, engine='openpyxl')

print(f"Links saved to {file_name}.")