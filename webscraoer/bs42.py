import requests
from bs4 import BeautifulSoup

url= 'https://www.amazon.sa/gp/product/B088ZYNX1J/ref=ewc_pr_img_1?smid=AYF6K39ETHYS9&th=1'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}
response= requests.get(url, headers=header, params={'?smid':'AYF6K39ETHYS9&th'})

soup = BeautifulSoup(response.content,'html.parser')

name_of = soup.find('span', id='productTitle')

price= soup.find('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')

image = soup.find('img', class_='a-dynamic-image')

dis= soup.find('div', id='productDescription')

print(name_of.string.strip() )
print(price.get_text().strip())
print(image ['src'])
print(dis.get_text().strip())