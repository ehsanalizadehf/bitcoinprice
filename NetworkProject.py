
import time
import requests
import os
from bs4 import BeautifulSoup

url = "https://www.investing.com/crypto/"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.122 Safari/537.36'}
newreq = requests.Session()

try:

    def liveprice():
        os.system("color B")
        page = newreq.get(url , headers=headers)
        soup = BeautifulSoup(page.content , 'html.parser')
        Reader = soup.find('td' , {"class": "price js-currency-price"}).find('a' , {"class": "pid-1057391-last"}).text
        time.sleep(1)
        return Reader

    while True:
        print(liveprice())

except KeyboardInterrupt:
    print("you closed the app")