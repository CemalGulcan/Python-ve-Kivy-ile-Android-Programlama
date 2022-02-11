def Agirlik_Degerleri_Hesapla(urun_deger,urun_kapasite,UrunAdeti):
    agırlık_degerleri = []

    for i in range(int(UrunAdeti)):
        d = float(int(urun_deger[i]) / int(urun_kapasite[i]))
        agırlık_degerleri.append(d)

    return agırlık_degerleri