from urllib import request
import urllib
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/places/default/view/China-47'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# locate the area row
tr = soup.find(attrs={'id':'places_area__row'})
print (tr)
# locate the area tag
td = tr.find_all(attrs={'class':'w2p_fw'})
print (td)
for book in td:
    print (book.string)

#area = td.text # extract the text from this tag
#print (area)
