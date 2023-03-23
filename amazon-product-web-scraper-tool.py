#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: idrisibrahimerten
"""



import requests
from bs4 import BeautifulSoup

# Amazon üzerinde bulduğumuz ürünün, ürün linkini değişkenle tanımlıyoruz.
url = 'https://www.amazon.com.tr/gp/product/B0BL2PHJJ9/'

# Headers bilgisini değişkenle tanımlıyoruz.
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
          'Referer': 'https://www.google.com/',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'en-US,en;q=0.9'}

# Belirlediğimiz url değişkenine istekte bulunuyoruz.
response = requests.get(url, headers = header)

# Bir değişken oluşturarak HTML ayrıştırması yaparak değişkene tanımlıyoruz.
soup = BeautifulSoup(response.content, 'html.parser')

# Başlığı HTML yapısından alıyoruz ve başlık bilgisini değişkene tanımlıyoruz.
title_element = soup.find('span', {'class':'a-size-extra-large'})
title = title_element.text

# Ürün fiyat bilgisini alıyoruz.
price_element = soup.find('span', {'class': 'a-price-whole'})
price = price_element.text

# ürün resminin url bilgisini alıyoruz.
image_element = soup.select_one('#imgBlkFront')
image_url = image_element['data-a-dynamic-image']

# Ürün rating bilgisini alıyoruz.
rating_element = soup.find('span', {'class': 'a-icon-alt'})
rating = rating_element.text.strip()

# Print the product details
print(f"Ürün Başlığı: {title}")
print(f"Ürün Fiyatı: {price}")
print(f"Ürünün Image URL: {image_url}")
print(f"Ürünün Rating bilgisi: {rating}")