# headless 크롬은 브라우저를 띄우지 않고 백그라운드에서 빠르게 작업하는 것

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=3024x1964")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36)")

browser = webdriver.Chrome("./chromedriver", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/100.0.4896.75 Safari/537.36
id = browser.find_element_by_id("detected_value")
print(id.text)
browser.quit()