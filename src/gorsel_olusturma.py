def renk_secme(mesaj): #kullanıcıdan renk girişlerini almak için oluşturulan fonksiyon.
    #kullanıcıdan 0-255 arasındaki rgb değerlerini alacak.
    print(f"\n{mesaj} için rgb değerlerini giriniz(0-255): ")
    r = int(input("Kırmızı (R): ")) #kullanıcıdan kırmızının değerini alır.
    g = int(input("Yeşil (G): ")) #kullanıcıdan yeşil değerini alır.
    b = int(input("Mavi (B): ")) #kullanıcıdan mavi değerini alır.
    return(r, g, b) #alınan rgb değerlerini geri döndürür.


def ppm_gorsel_olustur(): #alınan değerler ile görseli olusturacak asıl fonksiyon.
    sayac = 1

    while True: #kullanıcı istemediği sürece uygulama çalışmayı devam ettirir.
        print("=== PPM Görsel Oluşturucu (Pixel Art Generator) ===")
        print("Desen seçenekleri: ")
        print("1) Satranç Tahtası Deseni")
        print("2) Renkli Bayrak (2 Yatay Çizgi) Deseni")
        print("3) İki Renk Arası Gradyan (Geçiş) Deseni")
        print("4) Çapraz Çizgi Deseni")
        print("5) Çapraz Örüntü Deseni")

        secim = int(input("Desen numarasını seçiniz (1, 2, 3, 4, 5): ")) #kullanıcıdan istediği deseni alacak.
        yukseklik = int(input("Görsel yüksekliğini giriniz: ")) #kullanıcıdan görselin yüksekliğini alacak.
        genislik = int(input("Görsel genişliğini giriniz: ")) #kullanıcıdan görselin genişiliğini alacak.

        renk1 = renk_secme("1. Renk") #önceden oluşturduğumuz renk alma fonksiyonu ile 1. rengi alıyoruz.
        renk2 = renk_secme("2. Renk") #önceden oluşturduğumuz renk alma fonksiyonu ile 2. rengi alıyoruz.

        dosya_adi = "ciktigorsel.ppm" #resmi oluşturacağımız dosaynın adı.

        with open(dosya_adi, "w", encoding="utf-8") as dosya: 
        #dosayayı asıl oluşturan ve resmi çizen kısım burası olacak. buradaki "w" dosayayı yazma modunda açar. encoding="utf-8" ise 
        #dosya yazılırken türkçe karakterler veya yorum satırlarının yaratabileceği sorunları önlemek içindir.
            dosya.write("P3\n")
            dosya.write(f"{yukseklik} {genislik}\n")
            dosya.write("255\n")

        #ardışık döngülerle pixelleri yazdırma
            for y in range(yukseklik):
                satir_pixelleri = []
                for x in range(genislik):
                    if secim == 1: #ilk desen olan satranç tahtası desenini çizdirme.
                        r, g, b = renk1 if (x+y)%2==0 else renk2

                    elif secim == 2: # ikinci desen olan renkli bayrak desenini çizdirme.
                        r, g, b = renk1 if y < yukseklik // 2 else renk2 

                    elif secim == 3: # üçüncü desen olan gradyan desenini çizdirme.
                        oran = x/(genislik -1) if genislik > 1 else 0
                        r = int (renk1[0] + (renk2[0] - renk1[0]) * oran )
                        g = int (renk1[1] + (renk2[1] - renk1[1]) * oran )
                        b = int (renk1[2] + (renk2[2] - renk1[2]) * oran )

                    elif secim == 4: # dördüncü desen olan çapraz çizgi desenini çizdirme
                        r, g, b = renk1 if (x + y) % 4 == 0 else renk2

                    elif secim == 5: # beşinci desen olan çapraz örüntü desenini çizdirme
                        r, g, b = renk1 if ((x+y) % 4 == 0) or ((x+y) % 6 == 0) else renk2

                    else:
                        r, g, b, = (0,0,0)

                    satir_pixelleri.append(f"{r} {g} {b}") #önceden oluşturduğumuz satir_pixelleri listesine r g b değerlerini ekler.

                dosya.write(" ".join(satir_pixelleri) + "\n") #satırlar boyunca hesaplanan tüm piksel renk değerlerini aralarına boşluk koyarak birleştirir.

        print(f"\n'{dosya_adi}' başarıyla oluşturuldu!")
        sayac+=1
        devam = input("\nBaşka bir görsel oluşturmak ister misiniz? (e/h): ").strip().lower()
        if devam not in ("e", "evet"): #kullanıcının devam etmek isteyip istememesine göre kodu bitirir.
            print("Program sonlandırılıyor.")
            break


if __name__ == "__main__": #bu kısım python dosyasının çalıştırılıp çalıştırılmadığını kontrol eder ve ppm_gorse_olustur() çağrısının yalnızca doğrudan çağırıldığında çalıştırışmasını sağlar.
    ppm_gorsel_olustur()



