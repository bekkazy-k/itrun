from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.find_all('a'))
# print(soup.find(id="link3"))

# from bs4 import BeautifulSoup
# import requests
# url = ('https://pypi.org/project/beautifulsoup4/')
# r = requests.get(url)
#
# soup = BeautifulSoup(r.text, "html.parser")
#
# print(soup.h2['class'])
# # print(soup.h2.string)
# print(soup.div['class'])
# print(soup.find_all("div", {"class": "project-description"})[0].p.string)

# from bs4 import BeautifulSoup
# import requests
# url = ("https://github.com/Daniiar070?tab=repositories")
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
#
# print(soup.h3['class'])
# print(soup.find_all("li", {"class"}))
# print(soup.find_all("h3"))
# print(soup.find_all("a"))

# print(soup.find_all("div", {"class": "project-description"})[0].p.string)
# print(soup.find_all("h3", {"class": "wb-break-all"})[0].a.string)
# print(soup.find_all("h3", {"class": "wb-break-all"})[1].a.string)
# print(soup.find_all("h3", {"class": "wb-break-all"})[2].a.string)
# print(soup.find_all("h3", {"class": "wb-break-all"})[3].a.string)
# from bs4 import BeautifulSoup
# import requests
# url = ("https://github.com/Daniiar070")
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# from bs4 import BeautifulSoup
# import requests
# url = ("https://github.com/Daniiar070?tab=repositories")
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# p = input("Введите логин: ")
# print(f"https://github.com/{p}?tab=repositories")
# if p == "Daniiar070":
#     for i in soup.find_all("h3", {"class": "wb-break-all"}):
#         print(i.a.string.replace(" ", ""), end="")












