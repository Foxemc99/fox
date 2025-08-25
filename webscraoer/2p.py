import requests
from bs4 import BeautifulSoup

url= 'https://www.amazon.sa/%D8%A7%D8%AA%D8%AC%D8%A7%D9%87%D8%A7%D8%AA-%D9%87%D9%8A%D9%86%D8%BA%D9%84%D9%88%D9%86%D8%AC%D8%8C-%D8%A8%D8%B1%D9%8A%D8%B7%D8%A7%D9%86%D9%8A-%D9%85%D8%AA%D8%B9%D8%AF%D8%AF%D8%A9%D8%8C-%D8%A7%D9%84%D9%83%D9%87%D8%B1%D8%A8%D8%A7%D8%A6%D9%8A/dp/B0DZC3G568/ref=sr_1_4_sspa?adgrpid=103946401633&dib=eyJ2IjoiMSJ9.pr5TocvfeYOX4_5sgULwn8F6bQXZ9jq-BtjPm5xZn904LanWWREstFFNek085He0GSYLW-DTrwWRYhuNnJ8_oBEujL5Xdo9fGHnbmY3lz4DmHNQDYuhGJkwdMqJ7O6fytE5SxRVc8WpGN9_81MRqiL3krqPcK23Uqzga2LY7U_JyDWBK8mU6k25b99dfPNb2K29kfZIDYKzx_shfnCnEOrRqHzeIsjHn6pMXvi2Fu-YB_8gG-xZmPbZi0-1PThlldT2MbU1y93cXwBvjarASttvARX8401GSC7LU-8sN54o.fgO5h0V5-_vxYkJvLrGFUl7CWgtMEkU0VMOc_dvfo-c&dib_tag=se&hvadid=672376396501&hvdev=c&hvlocphy=20989&hvnetw=g&hvqmt=e&hvrand=18204779971828027053&hvtargid=kwd-22096507123&hydadcr=10896_2205628&keywords=amazon%2Bsa&mcid=b26dca1274dc39eabd7ac98e36959172&qid=1756122399&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

header= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}

response= requests.get(url,headers=header, params={'?adgrpid':'103946401633&dib'})

soup= BeautifulSoup(response.content,'html.parser')

title= soup.find('span', id='productTitle')

price= soup.find('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')

dis= soup.find('div', id='detailBulletsWrapper_feature_div')

pictuer=soup.find('img', alt='سلك تمديد طاقة مع مفاتيح بـ 4 اتجاهات شديد التحمل بطول 5 متر من هينغلونج، كيبل بريطاني طويل للغاية يثبت على الحائط ومقابس متعددة، شريط طاقة للحماية من اندفاع التيار الكهربائي 13 أمبير/ 2990 واط')

print(title.string.strip())
print(price.get_text().strip())
print(pictuer ['src'])
print(dis.get_text().strip())