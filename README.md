# Patika Kız Başına Bootcamp Final Project by İmregül Kurt

# 📊 Power BI Veri Analizi Projesi

## 🎯 Proje Amacı

Bu proje kapsamında, çok tablodan oluşan bir satış verisi modeli üzerinden:
- SQL server kullanma ve bu server'a bağlanma
- Database oluşturma ve bu database'e tablo ekleme
- Veri modelleme
- DAX ile ölçü ve kolon oluşturma
- Power Query ile ön işleme
- Power BI ile görselleştirme  

üzerinde çalıştım.

---

## 📁 Kullanılan Veri Setleri

- Datasets: `siparis.csv`, `siparisdetay.csv`, `kullanicilar.csv`, `adres.csv`, `urunler.csv`, `bolgeler.csv`
- `bolgeler.csv` dosyası aşağıda belirtilen GitHub repository'sinden alındı:

https://github.com/yigith/TurkiyeSehirlerBolgeler/blob/master/txt/SehirlerBolgeler.txt

Not: Bu dosyayı python kullanarak ; separatörü ile ayrılmış bir CSV formatına çevirdim.

---

## 🧭 Marka Seçimi

Ben **Nestle** markasını seçtim ancak eklediğim **Slicer** yardımı ile sayfadan seçerek **Eti** ve **Ülker** markalarının grafikleri de görüntülenebilmekte.

---

## 🔗 Veri Modeli ve Bağlantılar

Model View üzerinde aşağıdaki ilişkiler kuruldu:

- urunler[ID] → siparisdetay[ITEMID] (single)
- siparisdetay[ORDERID] → siparis[ID] (both)
- siparis[USERID] → kullanicilar[ID] (single)
- siparis[ADDRESSID] → adres[ID] (single)
- adres[CITY] → bolgeler[il] (single)

"siparis" ile "siparisdetay" arasında "both" yön seçeneğini seçmem gerekti.

![](https://github.com/imku13/patika-data-project/blob/main/images/model_view.png)

---

## 💻 Proje Kurulumum

- GitHub üzerinde bir repository açtım ve onu clone'ladım. Python kullanırsam diye bir venv ekledim.
- Docker üzerinden Microsoft SQL Server Express 2022 başlattım.
- Microsoft SQL Server Management Studio (SSMS) ile server'a localhost:1433
üzerinden bağlandım ve DataProjectDB adında bir database oluşturdum.
- CSV dosyalarını table olarak bu database'e ekledim.
- Power BI ile bu SQL Server üzerinden tabloları çekerek ilerledim.
- Gereken birkaç yerde Python kullanarak çeşitli düzenlemeler yaptım. (Türkçe karakter düzenlemesi gibi)

  
![](https://github.com/imku13/patika-data-project/blob/main/images/docker.png)

  
![](https://github.com/imku13/patika-data-project/blob/main/images/ssms.png)

  
---

## 🧼 Power Query Düzenlemeleri

- **kullanicilar tablosu:**
  - DAX ile doğum tarihi üzerinden yaş hesaplandı.
  - E veya K değerini alan conditional column eklendi.
  - NameSurname sütunu üzerinden Ad ve Soyad sütunları oluşturuldu.
  - Müşteri Sayısı, Erkek Müşteri Sayısı ve Kadın Müşteri Sayısı measure'ları eklendi.
- **adres tablosu:**
  - USERID ve CITY sütunlarının merge sütunu olan USERID-CITY sütunu eklendi.
- **Ürünler tablosu:**
  - Kategori isimleri düzenlendi (ANAKATEGORI, USTKATEGORI vs).
  - Bu tablodaki BRAND sütunu ile marka filtrelemesi yapıldı (Nestle).
- **siparisdetay tablosu:**
  - Müşteri Başına Adet ve Toplam Satış Adeti measure'ları eklendi.
- **siparis tablosu:**
  - DATE sütunu üzerinden Tarih ve Saat sütunları oluşturuldu.
  - Müşteri Başına Ciro, Ortalama Sipariş Tutarı, Sipariş Sayısı, Toplam Ciro measure'ları eklendi.
  - Gün Tipi (Hafta içi - Hafta sonu) ve Saat Dilimi (01:00 - 02:00 gibi) hesaplanan sütunları oluşturuldu.
- **bolgeler tablosu:**
  - Burada il sütununda Türkçe karakter sorunu vardı, onu Python ile adres tablosundaki CITY sütunu ile aynı formatta olacak şekilde düzenlemem gerekti.
  - Ayrıca dosyayı CSV'ye convert edince ilk satır görünmüyordu BLANK olarak geliyordu, onu çözmeye yönelik araştırma yaparken
utf-8-sig ile kaydederek dosyanın başında BOM (Byte Order Mark) olmamasını sağlamam gerekti.

---

## 🧮 Hesaplanan Kolonlar ve Ölçümlerin Bazıları

### Calculated Columns:
- **Gün Tipi:** Haftaiçi / Haftasonu ayırımı
- **Saat Dilimi:** "00:00 - 01:00" biçiminde saat dilimleri
- **YasGrubu:**  
  - 0–20 → GENÇ  
  - 21–34 → YETİŞKİN  
  - 35–54 → ORTA YAŞ  
  - 55+ → YAŞLI

---

### Measures:
- Toplam Satış Adeti  
- Toplam Ciro
- Toplam Sipariş Sayısı
- Toplam Müşteri Sayısı
- Müşteri Başına Ciro
- Müşteri Başına Adet
- Ortalama Sipariş Tutarı
- Erkek Sayısı, Kadın Sayısı (BRAND bazlı CALCULATE + FILTER kullanılarak)  

---

## 📊 Rapor Sayfaları ve Görselleştirmeler

### Giriş Sayfası
- Diğer sayfalara geçişi sağlayan butonlar

![](https://github.com/imku13/patika-data-project/blob/main/images/giris_sayfasi.png)

### Özet Sayfa
- **Grafikler:**
  - Haftaiçi vs. Haftasonu satış adeti
  - Saatlik satış (00:00–23:00 arası)
  - Bölgelere göre toplam satış adeti
- **Kartlar:**
  - Toplam Ciro
  - Toplam Müşteri Sayısı
  - Sipariş Sayısı
  - Ortalama Sipariş Tutarı
  - Müşteri Başına Ciro / Adet

![](https://github.com/imku13/patika-data-project/blob/main/images/ozet_sayfasi.png)

### Müşteri Perspektifi
- Tekil müşteri sayısı, erkek/kadın oranı
- Bölgelere göre müşteri dağılımı
- İstanbul’daki en yüksek ciroya sahip Top 10 müşteri
- Yaş grubuna göre satış grafiği

![](https://github.com/imku13/patika-data-project/blob/main/images/musteri_sayfasi.png)

### Kategori Perspektifi
- **TreeMap:** İstanbul’da yaşayan, genç yaş grubundaki müşterilerin kategorilere göre toplam cirosu

![](https://github.com/imku13/patika-data-project/blob/main/images/kategori_sayfasi.png)

---

## 🧾 PDF Rapor Çıktısı

Şu link üzerinden erişebilirsiniz: [dataproject.pdf](./dataproject.pdf).

---

## ❤️ Author

İmregül Kurt
