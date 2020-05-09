from selenium import webdriver
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def shopee():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Web Driver\chromedriver.exe')
    cari = 'lego'
    browserdriver.get('https://shopee.co.id/search?keyword=' + cari)
    content = browserdriver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    produk = soup.findAll('div', attrs={'class':'_3IHLHZ _2a6GrL'})
    # judul = soup.findAll('div', attrs={'class': '_1NoI8_ _16BAGk'})
    # rp = soup.findAll('span', attrs={'class': 'lwZ9D8'})
    # harga = soup.findAll('span', attrs={'class': '_341bF0'})
    return render_template('index.html', produk=produk)

if __name__ == '__main__':
    app.run(debug=True)

