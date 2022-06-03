import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화
browser.get("https://flight.naver.com")

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
# # 이번 달 27일, 다음 달 28일 선택
time.sleep(1)
browser.find_elements_by_xpath(
"//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button/b")[0].click()

# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("28")[1].click()
while True:
    pass


##   HTML  변경으로 패스...   날짜정보를 xpath 안쓰고 못가져오겠음....