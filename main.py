import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = (
    "https://time.by/catalog/jewelry/serebryanye-yuvelirnye-ukrasheniya/?PAGEN_2={}"
)
page_number = 1

while True:
    url = URL_TEMPLATE.format(page_number)
    r = requests.get(url)
    if r.status_code != 200:
        print("The request status code is not 200. Exiting the program.")
        exit()

    soup = BeautifulSoup(r.text, "html.parser")

    jewels = soup.find_all("div", class_="products__item-wrap")
    last_a = soup.find_all("div", class_="pagination__itemss")[0].find_all("a")[-1]
    last_pag_page_int = int(last_a.text)

    for card in jewels:
        image_url = (
            "https://time.by"
            + card.find("div", class_="products__item-image").a.img["src"]
        )
        jewel_name = card.find("div", class_="products__item-title").a.text.strip()
        jewel_price = card.find("div", class_="products__item-price").text.strip()

    page_number += 1
    if page_number > 2:  # last_pag_page_int:
        break
