# 1.야구 순위
import requests
from bs4 import BeautifulSoup as bs
url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo"

html = requests.get(url)
soup = bs(html.text, "html.parser")

# print(soup)

ranking = soup.find_all("tbody", id = "regularTeamRecordList_table")[0]

row = ranking.find_all("tr")

for item in row :
  team = item.find_all("th") [0]
  names = item.find_all("div")[0]
  print(f"{team.text}위 : {names.text}")


# 2.공조 한줄평
import requests
from bs4 import BeautifulSoup as bs

url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=201641"

html = requests.get(url)
soup = bs(html.text, "html.parser")
# print(soup)

reviews = soup.find_all("td", class_ = "title")
review_list = []

for i in reviews :
  review_list.append({"별점" : int(i.find('em').text), "감상평" : i.text.split('\n')[5]})

print(review_list)

for i, j in enumerate(review_list, start = 1) :
  print(f"{i}번 {j}")


# 3.네이버 뉴스 크롤링
# https://www.whatismybrowser.com/detect/what-is-my-user-agent

import requests
from bs4 import BeautifulSoup as bs

url = "https://n.news.naver.com/mnews/article/032/0003173706?sid=105"
hd = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
header = {"User-Agent" :hd}
html = requests.get(url, headers = header)
soup = bs(html.text, "html.parser")

title = soup.find("h2", class_ = "media_end_head_headline")
box = soup.find("div", id= "dic_area")

box.find("strong").decompose()  #strong 찾고 decompose() 메소드를 사용하면 해당 태그를 지워줌
box.find("span").decompose() #span 찾고 decompose() 메소드로 지워줌
news = ""

for i in box :
  text = i.string #.text와 .string의 차이 : string은 태그 하위에 있는 문자열만 반환
                 # text는 태그 하위의 자식태그에 있는 문자열까지 반환

  if text != None :   #Nonetype
    news += text
    

print("뉴스제목 : ", title.text)
print("뉴스기사 : ", news.strip())


# 네이버 뮤직 차트 순위 크롤링
import requests
from bs4 import BeautifulSoup as bs
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%AE%A4%EC%A7%81"

html = requests.get(url, headers = header)
soup = bs(html.text, "html.parser")

songs = soup.find_all("li", class_ = "list_item _sap_item _svp_item")

title = soup.find_all("div", class_ = "link_tit")

title_list = []

for i in songs :
  ranks = (i.find_all("em")[0]).text
  titles = (i.find_all("a")[0]).text
  singers = (i.find_all("span", class_ = "name")[1]).text

  print(f"{ranks}위 {singers}, 노래제목 : {titles}")