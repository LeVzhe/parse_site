import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = "http://seasonvar.ru/"
request = requests.get(URL_TEMPLATE)

if request.status_code != 200:
    print("The request status code is not 200. Exiting the program.")
    exit()

soup = BeautifulSoup(request.text, "html.parser")

site_content = soup.find_all("div", class_="news")

for new in site_content:
    new_head_class = new.find("div", class_="news-head")
    a_tags = new.find_all("a")
    print(new_head_class.text)
    print("--------------")

    for a_tag in a_tags:
        str = (
            "* "
            + a_tag.find("div", class_="news_n").text.replace("\n", "").strip()
            + " | "
            + a_tag.find("span", class_="news_s").text.replace("\n", "").strip()
        )
        print(str)
