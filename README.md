# Amazon Ürün Bilgisi Çekme Scripti / Amazon Product Scraper

Medium Text : https://medium.com/p/cf0b4c62840f

---

## English

### Description
This Python script retrieves product details (title, price, image URL, rating) from an Amazon product page using `requests` and `BeautifulSoup`. It is designed for educational and personal use; be sure to follow Amazon’s terms of service.

### Features
- Fetch product title  
- Fetch product price  
- Fetch product image URL  
- Fetch product rating  

### Requirements
- Python 3.6+  
- `requests` library  
- `beautifulsoup4` library  

Install dependencies with:
```bash
pip install requests beautifulsoup4
```

### Usage
1. Clone or download this repository.  
2. Open `amazon_scraper.py` (or your script name) and set the target URL:
   ```python
   url = 'https://www.amazon.com.tr/gp/product/B0BL2PHJJ9/'
   ```
3. (Optional) Adjust `header` to rotate user‐agents or modify headers.  
4. Run the script:
   ```bash
   python amazon_scraper.py
   ```
5. See printed output:
   ```
   Ürün Başlığı: …
   Ürün Fiyatı: …
   Ürünün Image URL: …
   Ürünün Rating bilgisi: …
   ```

### Notes
- Amazon frequently updates its page structure; if selectors break, inspect the HTML and update the `find`/`select` queries.  
- Consider adding delays or proxies to avoid being blocked.

---

## Türkçe

### Açıklama
Bu Python script’i, `requests` ve `BeautifulSoup` kütüphanelerini kullanarak bir Amazon ürün sayfasından başlık, fiyat, resim URL’si ve rating bilgilerini çeker. Eğitim ve kişisel kullanım amaçlıdır; Amazon’un kullanım şartlarına dikkat ediniz.

### Özellikler
- Ürün başlığını alır  
- Ürün fiyatını alır  
- Ürün resim URL’sini alır  
- Ürün rating bilgisini alır  

### Gereksinimler
- Python 3.6+  
- `requests` kütüphanesi  
- `beautifulsoup4` kütüphanesi  

Bağımlılıkları yüklemek için:
```bash
pip install requests beautifulsoup4
```

### Kullanım
1. Bu dizini klonlayın veya indirin.  
2. `amazon_scraper.py` (veya script adınız) dosyasını açın ve hedef URL’i ayarlayın:
   ```python
   url = 'https://www.amazon.com.tr/gp/product/B0BL2PHJJ9/'
   ```
3. (İsteğe bağlı) `header` değişkenini farklı User-Agent’lar eklemek veya başlıkları değiştirmek için güncelleyebilirsiniz.  
4. Script’i çalıştırın:
   ```bash
   python amazon_scraper.py
   ```
5. Çıktıyı ekranda görürsünüz:
   ```
   Ürün Başlığı: …
   Ürün Fiyatı: …
   Ürünün Image URL: …
   Ürünün Rating bilgisi: …
   ```

### Notlar
- Amazon sayfa yapısını zaman zaman günceller; CSS seçiciler çalışmazsa HTML’i inceleyip `find`/`select` sorgularını güncelleyin.  
- Engellenmeyi önlemek için isteklere gecikme ekleyebilir veya proxy kullanabilirsiniz.
