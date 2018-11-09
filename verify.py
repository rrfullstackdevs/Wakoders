#fonte de estudo https://www.youtube.com/watch?v=XQgXKtPSzUI

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#site exmeplo para web scraping
my_url = 'https://www.folhabv.com.br/noticia/Servidores-fazem-manifesto-em-frente-ao-TJRR/46132'

# download do site
uClient = uReq(my_url)
#ler e guarda o html raw
page_html = uClient.read()
#fecha
uClient.close()

page_soup = soup(page_html, "html.parser")

mytext = soup.findAll("div", {"class": "text"})