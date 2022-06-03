from venv import create
import requests
import re
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")

    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hC0BqsprvN8sscfVe44ssssss2C-213830"
    soup = create_soup(url)

    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    current_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text()
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    rain = soup.find("li", attrs={"class":"week_item today"}).find_all("span", attrs={"class":"weather_inner"})
    morning_rain = rain[0].get_text()
    evening_rain = rain[1].get_text()
 
    print(cast)
    print(current_temp)
    print(min_temp)
    print(max_temp)
    print(morning_rain)
    print(evening_rain)
    print()

def scrape_headline():
    print("[헤드라인 뉴스]")

    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)

    heads = soup.find_all("div", attrs={"class":"cluster_group _cluster_content"})

    for i in range(5):
        link = heads[i].find("a", attrs={"class":"cluster_text_headline nclicks(cls_sci.clsart)"})["href"]
        title = heads[i].find("a", attrs={"class":"cluster_text_headline nclicks(cls_sci.clsart)"}).get_text()
        print("{}. {}".format(i + 1, title))
        print("\t링크 : {}".format(link))
    print()

def scrape_eng():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)

    todays = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("영어지문")
    for sent in todays[len(todays)//2:]:
        print(sent.get_text().strip())
    print()
    print("한글지문")
    for sent in todays[:len(todays)//2]:
        print(sent.get_text().strip())
    print()

if __name__ == "__main__":
    scrape_weather()
    scrape_headline()
    scrape_eng()