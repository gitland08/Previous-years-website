import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "http://library.ddn.upes.ac.in:8081/upeslib/questionbank/soc/btech_AI.html"

# For getting the HTMl
r = requests.get(url)
htmlContent = r.content
# HTML parser
soup = BeautifulSoup(htmlContent, 'html.parser')

list2=[]
list3=[]
list4=[]

for link in soup.find_all('a'):
    list2.append(link.get('href'))

del list2[0:9]
del list2[0]
print(list2)




