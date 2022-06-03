from email.quoprimime import header_decode
import requests

headers = {"User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
url = "https://nadocoding.tistory.com"
res = requests.get(url, headers=headers)

res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)

