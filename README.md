# BLM101_26360859026_NisaBagci
Bursa Teknik Üniversitesi Bilgisayar Mühendisliğine Giriş Dönem Projesi

## Öğrenci Bilgileri
**Ad**: Nisa  
**Soyad**: Bağcı  
**Öğrenci Numarası**: 26360859026  

## Proje Konusu  
Python ile ppm formatında görsel oluşturan program yapma.  

## Kurulum Ve Çalıştırma  

### Gereksinimler
**Python sürümü**: 3.14 veya üzeri  
**Çıktı görselini görüntüleme**: Oluşturulan ppm dosyalarını doğrudan Visual Studio Code içinde açmak için **PBM/PPM/PGM Viewer for Visual Studio Code** eklentisi kullanılabilir.

### Kurulum Adımları
 Repoyu bilgisayarınıza klonlayın:  
 '''bash  
   git clone <REPO_LINKI>  
   cd <REPO_KLASOR_ADI>  

### Çalıştırma 
Ana dosyayı çalıştırmak için terminale **"src/gorsel_olusturma.py"** yazınız.


## Proje Ve Algoritma Açıklaması  

### Kod Mimarisi  
**Dosya ve Klasör Yapısı:** Programı oluşturan asıl kodların hepsi src dosyasının içinde bulunan gorsel_olusturma.py'nin içinde bulunmaktadır. Program çalıştırıldığında **"ciktigorsel.ppm"** dosyasını üretir. Proje modüler (fonksiyon tabanlı) bir yapıya sahiptir.  

### Fonksiyonların Amaçları  
**renk_secme:** Bu fonksiyonun amacı kullanıcıdan alınan renk değerlerini saklamak. Program sürekli tekrar çalışatırılabileceğinden ve renklerin sürekli tekrar kullanılması gerekeceğinden dolayı bu fonksiyonu oluşturdum.  Kullanılan if else yapıları rgb değerlerinin aralığını belirtmek içindir. RGB değerleri 0-255 arasında olacağından dolayı kullanıcı bu değerler harici bir değer girdiğinde değeri tekrar istemektedir. try-except yapısı ise hata alındığında o hatayı yakalayarak kodun bitmemesi içindir. Tanımlanan değerler int türünden olduğundan dolayı sayı harici bir şey girildiğinde valueerror yaşanmaktadır. Bu yaoı ile beraber böyle bir durum oluştuğunda kullanıcıya değerin geçerisz olduğu ve tekrar girilmesi söylenir. Böylece hata ile kod sonlanmamış olur.

**ppm_gorsel_olustur:** Asıl görseli oluşturan, kullanıcının desen seçeneğini alan kısmın hepsi bu fonksiyonun içindedir. 




   
