import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://www.melon.com/chart/index.htm"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

response = requests.get(url, headers = header)
soup = bs(response.text, "html.parser")

rank1 = soup.find_all("div", class_ = "ellipsis rank01")
rank2 = soup.find_all("span", class_ = "checkEllipsis")

song = []
singer = []

for i, j in zip(rank1, rank2) :
    song.append(i.text)
    singer.append(j.text)
rank = [i for i in range(len(song))]

f = open("melon.csv", "w", newline = "", encoding = "utf-8")
# writer = csv.writer(f)

# col_names = [["순위", "노래제목", "가수"]]
# for row in col_names :
#     writer.writerow(row)
    
# csv 파일로 저장
fields = ["rank", "song", "singer"]
wt = csv.DictWriter(f, fieldnames = fields)
wt. writeheader()

for rank, song, singer in zip(rank, song, singer) :
    wt.writerow({"rank" : rank +1, "song" : song, "singer" : singer})