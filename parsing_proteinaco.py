import requests
from bs4 import BeautifulSoup
import fake_useragent
from time import sleep
import os

user = fake_useragent.UserAgent().random
headers = {
    "User-Agent": user}


def download(url):
    resp = requests.get(url, stream=True)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_folder = os.path.join(script_dir, "images")
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    r = open(os.path.join(image_folder, url.split("/")[-1].split("?")[0]), "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_url():
    for count in range(1, 5):
        url = f"https://www.proteinaco.cz/oriskova-masla/strana-{count}/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="product")

        for i in data:
            card_url = "https://www.proteinaco.cz" + i.find("a").get("href")
            yield card_url


def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="p-detail-inner")
        name = data.find("h1").text.strip()
        price = data.find("span", class_="price-final-holder").text.strip()
        text = data.find("div", class_="p-short-description").text
        url_img = data.find("img").get("src")
        download(url_img)
        yield name, price, text, url_img


array()