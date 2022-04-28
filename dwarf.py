from bs4 import BeautifulSoup
import requests
import pandas as pd

starturl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

headers = ["name","distance","mass","radius"]
data = []

page = requests.get(starturl)
soup = BeautifulSoup(page.text,"html.parser")

startable = soup.find_all("table")

templist = []
trtags = startable[5].find_all("tr")

for tr in trtags :
    tdtags = tr.find_all("td")
    row = [i.text.rstrip() for i in tdtags]    
    templist.append(row)

print(templist)

names = []
distance = []
radius = []
mass = []


for i in range(1,len(templist)) :
    names.append(templist[i][0])
    distance.append(templist[i][5])
    radius.append(templist[i][8])
    mass.append(templist[i][7])


DF = pd.DataFrame(list(zip(names,distance,mass,radius)),columns=["Star_Name","Distance","Mass","Radius"])
DF.to_csv("dwarf.csv")