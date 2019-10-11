from bs4 import BeautifulSoup
import requests

#url = ("https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html")
url = "https://docs.python.org/fr/2.7/howto/regex.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')    #or just soup.p
first_paragraph_text = soup.p.text

print(first_paragraph_text)
