# 1000kitap.com Yazar Bilgileri
## **1000kitap.com'da bulunan istediğiniz Yazara ait bilgileri yazdırır. #poowww!!!**
![This is an image](https://www.imagevisit.com/images/2022/12/11/ggg.gif)

### Kullanılan Kütüphaneler
1. httpx
2. rich
3. BeautifulSoup4

### İndirmeniz Gereken Kütüphaneler
 ```
pip install httpx
pip install rich
pip install beautifulsoup4

```
Bu projeyi öğrendiklerimi pekiştirmek amacıyla yazdım. Kısaca projenin mantığı 1000kitap.com'a kullanıcıdan alınan Yazar bilgileri (ad ve soyad) get isteği ile gönderilir, gelen yanıttan beautifulsoup4 kütüphanesi ile html pars işlemleri yapılıp Yazar bilgileri (Hakkında, Unvan, Doğum Bilgileri ve Yazara ait 5 eseri) konsola yazar. 

Kullanıcıdan alınan veri **lower()** metodu ile karakterleri küçültüp, **replace()** metodu ile boşlukları **-** ile değiştirip son olarak türkçe karakterleri dönüştürdüm url yapısına uygun olması için. Bazı kontrol şartları oluşturdum: boş veri kontrolü, kullanıcıdan alının verinin karakter sayı kontrolü, kullanıcının girdiği yazar verisi bulunamadığında hata mesajı kontrolü (error handling)

## Umarım kendimi Programlama da geliştirir, çok daha iyi projelerle github profilimi doldururum.  :smiley:

Projeye ait görsel: :point_down:	

![This is an image](https://www.imagevisit.com/images/2022/12/11/pow.png)

	
