import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument("--incognito")
options.add_argument("--window-size=1920x1080")
options.add_argument('disable-infobars')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.set_script_timeout(60*60*24)
driver.get("https://oto.com.vn/mua-ban-xe")
last_height = driver.execute_script("return document.body.scrollHeight")
count = 1

# load until end of page
while True:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)
	loadmore = driver.find_element(by=By.XPATH, value='//*[@id="btnloadmore"]')
	driver.execute_script("arguments[0].click();", loadmore)

	new_height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
	last_height = new_height
	count += 1
	print(count)

a = driver.find_elements(by=By.CSS_SELECTOR, value='.item-car')
# ['ten', 'gia', 'nam sx', 'so km da di', 'loai hop so', 'xuat xu', 'ng ban', 'dia diem']
header = ['Title', 'Price', 'Since', 'Distance', 'Gearbox', 'Origin', 'Seller', 'Location']
num_row = 0

with open('cars.csv', 'w', encoding='utf8', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(header)

	for obj in a:
		title = obj.find_element(by=By.CSS_SELECTOR, value='div.info h3.title a').text.split(' - ')[0]
		price = obj.find_element(by=By.CSS_SELECTOR, value='div.info p.price').text
		price = ' '.join([price.split(' triệu ')[0], 'triệu'])
		ul = obj.find_elements(by=By.CSS_SELECTOR, value='ul.info-car li')
		if len(ul) == 4:
			since = ul[0].text
			distance = ul[1].text
			gearbox = ul[2].text
			origin = ul[3].text
		elif len(ul) == 3:
			since = ul[0].text
			distance = "null"
			gearbox = ul[1].text
			origin = ul[2].text
		seller = obj.find_element(by=By.CSS_SELECTOR, value='span.user-name').text
		location = obj.find_element(by=By.CSS_SELECTOR, value='div.loca').text
		writer.writerow([title, price, since, distance, gearbox, origin, seller, location])
		num_row += 1

print("count loadmore: ", count)
print("num rows: ", num_row)
print("DONEEE")
driver.quit()
