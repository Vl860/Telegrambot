from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()

# General price getter function
def getvalue(url):
    r = s.get(url)
    page = BeautifulSoup(r.text, "html.parser")
    currencyprice = page.find("span", {"class": "DFlfde SwHCTb"}).text
    return currencyprice


#US-Dollar price
class USD:
    value = getvalue("https://www.google.com/search?q=usd+in+chf")

# Euro price
class EUR:
    value = getvalue("https://www.google.com/search?q=eur+in+chf")

# Japanese yen price
class JPY:
    value = getvalue("https://www.google.com/search?q=jpy+in+chf")

# Pound sterling price
class GBP:
    value = getvalue("https://www.google.com/search?q=gbp+in+chf")

# Australian dollar price
class AUD:
    value = getvalue("https://www.google.com/search?q=aud+in+chf")

# Canadian dollar price
class CAD:
    value = getvalue("https://www.google.com/search?q=cad+in+chf")

# Hong Kong dollar price
class HKD:
    value = getvalue("https://www.google.com/search?q=hkd+in+chf")

# New Zealand dollar price
class NZD:
    value = getvalue("https://www.google.com/search?q=nzd+in+chf")



# normal check
if __name__ == "__main__":
    print("Hello")
