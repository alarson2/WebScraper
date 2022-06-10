from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphics+card'

# Grabbing the web page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Parsing HTML
page_soup = soup(page_html, "html.parser")

# Grabs each item
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "product-name, price\n"

f.write(headers)

for container in containers:
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    price_container = container.findAll("li", {"class":"price-current"})
    price = price_container[0].text.strip()

    print("product_name: " + product_name)
    print("price: " + price)

    f.write(product_name.replace(",", "|") + "," + price.replace(",", "") + "\n")

f.close()