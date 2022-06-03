import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") ##### res를 lxml을 통해 beautifulsoup이라는 객체화. 변수명 soup
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a
# print(soup.a.attrs) # a 의 속성
# print(soup.a["onclick"]) # a 엘리먼트의 onclick 속성값

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) #class 값이 Nbtn_upload인 a elent를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank3.a.get_text())
# print(rank2.a.get_text())

# print(rank1.parent)

# ttest = soup.find("ol", attrs={"class":"asideBoxRank"})
# print(ttest)
# print(rank1.a.get_text())
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# siblings = rank1.find_next_siblings("li")
# print(siblings)

webtoon = soup.find("a", text="싸움독학-125화 : 독종 한왕국")
print(webtoon)