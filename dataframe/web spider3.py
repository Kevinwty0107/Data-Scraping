import urllib
from urllib import request
from bs4 import BeautifulSoup

res = urllib.request.urlopen("https://www.bloomberg.com/quote/SPX:IND")
soup = BeautifulSoup(res,"html.parser")
#print(soup)
#print('\n' * 2)
price_box = soup.find_all(attrs={"class":"price"})
print (price_box)
for p in price_box:
    print (p.string)


#book_div = soup.find(attrs={"id":"root"})
#print(book_div)
#print('\n' * 2)
#book_a = book_div.find_all(attrs={"class":"price"})
#print(book_a)
#for book in book_a:
   # print (book.string)