import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://vibe.naver.com/chart/total"
driver.get(url)
html = driver.page_source
soup = bs(html, "html.parser")

song_box = soup.find("tbody")
songs = song_box.select("td.song")

song_rank = []
rank = 1
for song in songs :
    ranks = str(rank) + "위"
    title = song.select_one("a.link_text").get("title")
    singers = song.select_one("a.link_artist").text
    song_rank.append([ranks, title, singers])
    rank += 1
    
print(song_rank)

f = open("vibe.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(f)

col_names = [["순위", "노래제목", "가수"]]
for row in col_names :
    writer.writerow(row)
    
for row in song_rank :
    writer.writerow(row)
    
f.close()