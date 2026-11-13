import requests, csv
from bs4 import BeautifulSoup

res = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(res.text,"html.parser")

with open ("books.csv","w") as f:
 w = csv.writer(f)
 w.writerow(["Title","price"])
 for b in soup.find_all("article",class_="product_pod"):
  w.writerow([b.h3.a["title"],b.find("p",
class_="price_color").text])

print("Done!")
