from ast import Num
from cgi import print_exception
import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%EB%8F%84+%ED%91%B8%EB%A5%B4%EC%A7%80%EC%98%A4"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

forms = soup.find_all("td", attrs={"class":"col1"})
surfs = soup.find_all("td", attrs={"class":"col2"})
prints = soup.find_all("td", attrs={"class":"col3"})
nums = soup.find_all("td", attrs={"class":"col4"})
floors = soup.find_all("td", attrs={"class":"col5"})

data = []
data.append(soup.find_all("td", attrs={"class":"col1"}))
data.append(soup.find_all("td", attrs={"class":"col2"}))
data.append(soup.find_all("td", attrs={"class":"col3"}))
data.append(soup.find_all("td", attrs={"class":"col4"}))
data.append(soup.find_all("td", attrs={"class":"col5"}))


for i in range(1, 6):
    print("="*5, "매물", i, "="*5)
    print("거래 :", data[0][i-1].get_text())
    print("면적 :", data[1][i-1].get_text())
    print("가격 :", data[2][i-1].get_text())
    print("동 :", data[3][i-1].get_text())
    print("층 :", data[4][i-1].get_text())

with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for idx, row in enumerate(data_rows):
    columns = row.find_all("td")
    print("=" * 8, "매물{}".format(idx + 1), "=" * 8)
    print("거래 :", columns[0].get_text().strip())
    print("면적 :", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 :", columns[2].get_text().strip(), "(만원)")
    print("동 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())