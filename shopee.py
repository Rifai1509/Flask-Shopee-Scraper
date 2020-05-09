from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')

browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Web Driver\chromedriver.exe')

cari = 'lego'
browserdriver.get('https://shopee.co.id/search?keyword='+cari)
content = browserdriver.page_source
soup = BeautifulSoup(content, 'html.parser')
judul = soup.findAll('div', attrs={'class':'_1NoI8_ _16BAGk'})
mataUang = soup.findAll('span', attrs={'class':'lwZ9D8'})
harga = soup.findAll('span', attrs={'class':'_341bF0'})
produk = soup.findAll('div', attrs={'class':'_1gkBDw _2O43P5'})

hitung = 0
for x in range(0, len(judul)):
    hitung +=1
    print('{0}. {1}\n   {2} {3}'.format(hitung,judul[x].text.strip(), mataUang[x].text.strip(), harga[x].text.strip()))