import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://www.melon.com/chart/index.htm"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

response = requests.get(url, headers = header)
soup = bs(response.text, "html.parser")

li = []

songs = soup.find_all("tr", calss_ = "lst50")
for i in songs :
    ranks = (i.find_all("span", class_ = "rank")[0]).text + (i.find_all("span", class_ = "none")[0]).text
    titles = (i.find_all("a")[2]).text
    singers = (i.find_all("a")[3]).text
    li.append([ranks, titles, singers])
    
    print(f"{ranks}: 노래제목 : {titles} 가수 : {singers}")
    
f = open("melon1.csv", "w", newline = "", encoding = "utf-8")
writer = csv.writer(f)

col_names = [["순위", "노래제목", "가수"]]
for row in col_names :
    writer.writerow(row)

for row in li :
    writer.writerow(row)

f.close()