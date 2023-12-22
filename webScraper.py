import requests
from bs4 import BeautifulSoup

url = 'https://freedium.cfd/https://medium.com/python-in-plain-english/how-i-made-money-with-python-3-web-scraping-c1f2db963ead?source=search_post---------1----------------------------'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title')
text = soup.get_text()
links = [link.get('href') for link in soup.find_all('a')]
table = soup.find('table')
headers = [header.get_text() for header in table.find_all('th')]
rows = []
for row in table.find_all('tr'):
    rows.append([data.get_text() for data in row.find_all('td')])
print(headers)
print(rows)