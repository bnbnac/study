import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver")

# 1. 네이버로 이동
browser.get("https://www.naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 아이디 패스워드 입력
browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("pw").send_keys("pw")

# 4. 로그인 버튼 클릭
elem = browser.find_element_by_id("log.login").click()

time.sleep(1)

# 5. 아이디를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("new_id")

# 6. 로그인 후 html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit()
# browser.quit() 현재 탭만 종료


# # 바로 닫히는거 막는 법을 몰라서;
# while True:
#     pass