import requests
import bs4

import pdb

# result = requests.get("http://www.example.com")

# soup = bs4.BeautifulSoup(result.text, "lxml")

# # print(soup)

# titleTag = soup.select("title")

# print(type(titleTag))

# for tag in titleTag:
#   print(tag.getText(), type(tag))

# titleTag = soup.select("p")

# for tag in titleTag:
#   print(tag.getText())

tamilResult = requests.get("https://en.wikipedia.org/wiki/Tamil_language")

tamilSoup = bs4.BeautifulSoup(tamilResult.text, 'lxml')

tamilTable = tamilSoup.select('#toc .toctext')

tamilTable[0] 

# print(tamilTable)

for tamilRow in tamilTable:
  print(tamilRow.getText())


for img in tamilSoup.select(".thumbimage"):
  print(img['src '])


from PIL import Image

word_matrix = Image.open("word_matrix.png")
mask = Image.open("mask.png")

mask.re
