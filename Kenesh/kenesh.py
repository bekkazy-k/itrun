from bs4 import BeautifulSoup
import requests


url = "http://kenesh.kg/ky/deputy/list/35"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
deputy = soup.find_all("div", class_="col-xs-12")
pages = soup.find('ul', class_='pagination')
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text)