import requests
import os
from bs4 import BeautifulSoup
import re


def download(url_,file_path="./md/"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    res = requests.get(url_, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    shuju = soup.find_all(name='a', attrs={'href': re.compile('^bug_detail\.php')})
    for i in shuju:
        url_ = i['href']
        url_1 = "https://wy.zone.ci/" + url_
        res_ = requests.get(url_1, headers=headers)
        html_ = res_.content
        with open(file_path + url_.split("=")[-1]+".md", "wb") as f:
            f.write(html_)
        print("下载成功")


url = "https://wy.zone.ci/searchbug.php?q=SQL&page=1"
download(url)
# for i in range(1, 10):
#     url = f"https://wy.zone.ci/searchbug.php?q=SQL&page={i}"
#     download(url)

