import numpy as np


class KnapsackDeger:
    def __init__(self, isim ,kapasite, deger):
        self.kapasite = kapasite  # Agirlik
        self.deger = deger  # Deger
        self.isim = isim

    def __repr__(self):
        return "Ürün İsmi : " + str(self.isim) + " , Kapasitesi: " + str(self.kapasite) + ", Değeri: " + str(self.deger)

class Knapsack:
    def __init__(self, toplam_kapasite):
        self.toplam_kapasite = toplam_kapasite  # Agirlik limiti
        self.degerler = []  # esyalar

    def DegerEkle(self, deger):
        self.degerler.append(deger)

    def DegerlerEkle(self, degerler):
        for deger in degerler:
            self.DegerEkle(deger)

    def Dinamik_Sonuc(self):
        deger_sayisi = len(self.degerler)  # esya sayisi
        sonuc_matrisi = np.zeros([deger_sayisi + 1, self.toplam_kapasite + 1])
        for i in range(0, self.toplam_kapasite + 1):  # her satir icin
            for k in range(1, deger_sayisi + 1):  # her sutun icin
                if self.degerler[k - 1].kapasite < i + 1:  # Formulasyon
                    sonuc_matrisi[k][i] = max(self.degerler[k - 1].deger + sonuc_matrisi[k - 1][i - self.degerler[k - 1].kapasite], sonuc_matrisi[k - 1][i])
                else:
                    sonuc_matrisi[k][i] = sonuc_matrisi[k - 1][i]
        return sonuc_matrisi  # matrisi dondur

    def Urun_isimleri(self):
        sonuc_matrisi = self.Dinamik_Sonuc()
        urun_listesi = []
        i = -1;
        j = -1
        top_satır = len(sonuc_matrisi)
        top_sutun = len(sonuc_matrisi[-1])
        while i != -top_satır and j != -top_sutun:
            if sonuc_matrisi[i][j] == sonuc_matrisi[i][j - 1]:
                j -= 1
            elif sonuc_matrisi[i][j] == sonuc_matrisi[i - 1][j]:
                i -= 1
            else:
                urun_listesi.append(self.degerler[i])
                j -= self.degerler[i].kapasite
                i -= 1

        return urun_listesi
