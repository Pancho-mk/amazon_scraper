import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.de/dp/B081ZD6ZP4/ref=sr_1_4?crid=2WKA5QHB671Y8&keywords=acer+aspire+5&qid=1585549204&refinements=p_n_operating_system_browse-bin%3A392677011%7C491361011&rnid=392676011&s=computers&sprefix=acer+%2Caps%2C314&sr=8-4'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}

def checkprice():

	page = requests.get(url, headers=headers)

	soup = BeautifulSoup(page.content, 'lxml')

	title = soup.find(id = "productTitle").get_text()  

	price = soup.find(id = "priceblock_ourprice").get_text()

	converted_price = int(price[0:3])
	print(converted_price)

	if converted_price < 750:
		send_mail()

	print(title.strip())

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()   # it encrypt the connection
	server.ehlo()

	server.login('your_mail', 'your_pasword')
	subject = 'Price fell down'
	body = 'Check the Amazon link: https://www.amazon.de/dp/B081ZD6ZP4/ref=sr_1_4?crid=2WKA5QHB671Y8&keywords=acer+aspire+5&qid=1585549204&refinements=p_n_operating_system_browse-bin%3A392677011%7C491361011&rnid=392676011&s=computers&sprefix=acer+%2Caps%2C314&sr=8-4'
	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'your_mail',
		'delivery_mail',
		msg
	)
	print('Email has been sent')
	server.quit()

while (True):
	checkprice()
	time.sleep(60 * 60 *24)             # check price every 24 hours









