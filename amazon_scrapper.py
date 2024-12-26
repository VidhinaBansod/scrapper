import requests
from bs4 import BeautifulSoup

URL = input("Please enter url you want to Check:")

headers = {"user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/126.0.0.0"
                         "Safari/537.36"}


def getting_data():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    #it is for title don't edit
    title = soup.find(id="productTitle").get_text()
    print("Name = " + title.strip())
    print(".")

    #price
    def paise():
        price = soup.find("span", class_="a-price-whole")
        print("Price in rupees is :")
        for actual_price in price:
            actual_price = str(actual_price.text)
            print(actual_price)

    def kitna_hai():
        availability = soup.find_all("span", class_="a-size-medium a-color-success")
        for stock in availability:
            stock = str(stock.text)
            print("Availability = " + stock)
            print(".")

    def scene():
        cust_review = soup.find_all("span", class_="a-size-base a-nowrap")
        for review in cust_review:
            review = str(review.text)
            print("Review = " + review + "\n.")

    def brief_revs():
        brief = soup.find_all("p", class_="a-spacing-small")
        print("The brief review of product is as follows:")
        for x in brief:
            x = str(x.text)
            print(x)
        print(".")

    paise()
    kitna_hai()
    scene()
    brief_revs()


getting_data()
