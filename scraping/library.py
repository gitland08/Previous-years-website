import requests
from bs4 import BeautifulSoup
import csv

#Parse the html using beautiful soup
url = "http://library.ddn.upes.ac.in:8081/upeslib/questionbank.html"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
#Finding the "a" elements with class and store them in anchor list
anchors = soup.find_all('a',class_='LINK')
print(anchors[0])

#Creating an empty set
all_link = set()

#The links are added to set and passed into empty dictionary created
my_dict = {}
for link in anchors:
    if(link.get('href') != '#'):
        linktext =  link.get('href')
        all_link.add(link)
        my_dict[link.text] = linktext
print(my_dict)

#Dictionary data is saved in a csv file that is created
with open('library.csv', 'w') as f:
    for key in my_dict.keys():
        f.write("%s,%s\n"%(key,my_dict[key]))
