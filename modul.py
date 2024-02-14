import sqlite3 as sql 
import time 

class Kitap():
    
    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
        
    def __str__(self):
        return "Kitap ismi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaski: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)
    
class Kutuphane():

    def __init__(self):
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti = sql.connect("veritabani.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS Kitaplar (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Tür TEXT,Baski INTEGER)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):
        sorgu = "SELECT * FROM Kitaplar"
        self.cursor.execute(sorgu)
        Kitaplar = self.cursor.fetchall()
        
        if len(Kitaplar) == 0:
            print("Henüz böyle bir kitap bulunmuyor...")
        else: 
            for i in Kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):
        sorgu = "SELECT * FROM Kitaplar WHERE İsim = ?"
        self.cursor.execute(sorgu,(isim,))
        Kitaplar = self.cursor.fetchall()
        
        if len(Kitaplar) == 0:
            print("Henüz böyle bir kitap bulunmuyor...")

        else:
            kitap = Kitap(Kitaplar[0][0],Kitaplar[0][1],Kitaplar[0][2],Kitaplar[0][3],Kitaplar[0][4])
            print(kitap)

    def kitap_ekle(self,kitap):
        sorgu = "INSERT INTO Kitaplar VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit()
    
    def kitap_sil(self,isim):
        sorgu = "DELETE FROM Kitaplar WHERE İsim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baski_yukselt(self,isim):
        sorgu = "SELECT * FROM Kitaplar WHERE İsim = ?"
        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmuyor...")

        else:
            baski = kitaplar[0][4]
            baski += 1

            sorgu_2 = "UPDATE Kitaplar SET Baski = ? WHERE İsim = ?"
            self.cursor.execute(sorgu_2,(baski,isim))
            self.baglanti.commit()