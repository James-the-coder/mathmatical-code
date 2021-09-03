import bs4
import requests
from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring




def parsePrice():
  r = requests.get("https://finance.yahoo.com/quote/FB?p=FB")
  soup = bs4.BeautifulSoup(r.text, "lxml")
  price = soup.find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text
  return price

while True:
  print("Price is $" + str(parsePrice()))
