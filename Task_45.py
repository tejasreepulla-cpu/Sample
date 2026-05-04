import requests
import pandas as pd
from bs4 import BeautifulSoup

# response=requests.get("https://sportscorner.qa/en/mens/footwear.html?brand=5662")
# print(response)
# soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
# names=soup.find_all('a',class_='product-item-link')
# # print(names)

# name=[]
# for i in names[1:6]:
#     d=i.get_text(strip=True)
#     name.append(d)
# print(name)


# Prices
# prices=soup.find_all('span',class_='price')
# print(prices)
# price=[]
# for i in prices:
#     d=i.get_text()
#     d=d.replace('QR',' ').replace('\xa0',' ').strip()
#     price.append(float(d))
# print(price)

 
# response=requests.get("https://quotes.toscrape.com/")
# print(response)
# soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

# quotes=soup.find_all('span',class_="text")
# print(quotes)

# quote=[]
# for i in quotes:
#     d=i.get_text()
#     quote.append(d)
# print(quote)

# authors=soup.find_all('small',class_="author")
# # print(authors)

# author=[]
# for i in authors:
#     d=i.get_text()
#     author.append(d)
# print(author)

# data=pd.DataFrame()
# # print(data)

# data['quotes']=quote
# data['authors']=author
# print(data)
# data.to_csv("quotes.csv")

response=requests.get("https://books.toscrape.com/")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

prices=soup.find_all('p',class_="price_color")
# print(prices)

price=[]
for i in prices:
    d=i.get_text()
    d=d.replace('£',' ').strip()
    price.append(float(d))    
print(price)

data=pd.DataFrame()
# print(data)
data['prices']=price

data.to_csv("prices.csv")






