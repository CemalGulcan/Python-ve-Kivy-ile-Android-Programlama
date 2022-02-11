def Greedy_Algoritmasi_İsim(ToplamKapasite,urun_isim,urun_kapasite,urun_agirlikdegeri,UrunAdeti):
    son_degerler = []


    if UrunAdeti == 0 or ToplamKapasite == 0 :
          return son_degerler

    for i in range(0,len(urun_agirlikdegeri)):
        maksimum = 0
        for i in urun_agirlikdegeri:
            if maksimum < i:
                maksimum = i
        for i in range(0,len(urun_agirlikdegeri)):
            if maksimum == urun_agirlikdegeri[i]:
                indis = i
                break
        if urun_kapasite[indis] > ToplamKapasite:
            urun_isim.remove(urun_isim[indis])
            urun_kapasite.remove(urun_kapasite[indis])
            urun_agirlikdegeri.remove(urun_agirlikdegeri[indis])

        else:
            son_degerler.append(urun_isim[indis])
            ToplamKapasite = ToplamKapasite - urun_kapasite[indis]
            urun_isim.remove(urun_isim[indis])
            urun_kapasite.remove(urun_kapasite[indis])
            urun_agirlikdegeri.remove(urun_agirlikdegeri[indis])


    return son_degerler