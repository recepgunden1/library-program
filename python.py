from modul import *
print("""
*********************************
Kütüphane programına hoş geldiniz
1 - Kitapları görüntüle
2 - Kitap sorgulama
3 - Kitap ekle
4 - Kitap sil
5 - Baskı yükselt
6 - ÇIKIŞ
*********************************""")

kütüphane = Kutuphane()

while True:
    islem = input("İşleminizi giriniz: ")
    
    if islem == "6":
        kütüphane.baglantiyi_kes()
        print("Program sonlandırılıyor...")
        break

    elif islem == "1":
        kütüphane.kitaplari_goster()

    elif islem == "2":
        isim = input("Hangi kitabı sorgulamak istiyorsunuz: ")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)

    elif islem == "3":
        isim = input("Kitabın ismi: ")
        yazar = input("Yazarın ismi: ") 
        yayinevi = input("Yayınevi: ")
        tur = input("Türü:")
        baski = int(input("Baskı sayısı:"))
        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi")

    elif islem == "4":
        isim = input("Silmek istediğiniz kitabın adını giriniz: ")
        kütüphane.kitap_sil(isim)
        print("Kitap silindi...")

    elif islem == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz: ")
        print("Baskı yükseltildi...")
        kütüphane.baski_yukselt(isim)
    else:
        print("Geçersiz işlem...")
