import requests
from bs4 import BeautifulSoup
import time

url = 'https://bih.hch.gov.tw/web/page/news22-%E5%AD%95%E5%A9%A6%E7%96%AB%E8%8B%97%E9%96%80%E8%A8%BA%E5%85%AC%E5%91%8A.html'
headers = {
    "Authorization": "Bearer " + "ekuo8mZjzr3z00Lfk5ZQQwVWQPi9rh2VIJBg9NUBjnm", 
    "Content-Type" : "application/x-www-form-urlencoded"
}
html = requests.get(url)
html.encoding = 'utf8'
#print(html.text)
time.sleep(2)

soup = BeautifulSoup(html.text, 'html.parser')
w3schollsList = soup.find_all('body')
for w3scholl in w3schollsList:
    ulList = w3scholl.find_all('li')

for index,li in enumerate(ulList):
    #print(index)
    if(index >= 5):
        #print(li.getText())
        payload = {'message': li.getText() }
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)