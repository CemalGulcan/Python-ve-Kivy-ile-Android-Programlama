from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import greddy_agirlik
import greddy_deger
import greddy_isim
import greddy_kapasite
import greddy_sonuc
import dinamik_algoritma

Builder.load_string("""

#:kivy 1.11.0


<EkranYonetimi>:

    GirisEkrani:
        id: GirisEkrani
        name: 'Giriş Ekranı'
    UrunAlmaEkrani:
        id: UrunAlmaEkrani
        name: 'Ürün Alma Ekranı'


<GirisEkrani>:

    RelativeLayout:    

        Label:    
            id: canta_kapasitesi   
            text: 'Çanta Kapasitesi'  
            pos_hint: {'x': 0.1, 'y': 0.85}    
            size_hint: (0.15, 0.05)    
            font_size: (canta_kapasitesi.width + canta_kapasitesi.height) / 6  
            color : (0.41015625,0.54296875,0.41015625,1)
            bold: True

        TextInput:    
            id: canta_kapasitesi_input    
            text: ''    
            background_color: (0.37109375,0.37109375,0.37109375,1)   
            foreground_color: (0, 0, 0, 1)    
            pos_hint: {'x': 0.3, 'y': 0.83}   
            size_hint: (0.675, 0.1)   
            font_size: (canta_kapasitesi_input.width + canta_kapasitesi_input.height) / 24


        Label:    
            id: urun_kapasitesi   
            text: 'Ürün Sayısı'  
            pos_hint: {'x': 0.1, 'y': 0.55} 
            size_hint: (0.15, 0.05)   
            font_size: (canta_kapasitesi.width + canta_kapasitesi.height) / 6  
            color : (0.41015625,0.54296875,0.41015625,1)
            bold: True   

        TextInput:   
            id: urun_kapasitesi_input    
            text: ''  
            background_color: (0.37109375,0.37109375,0.37109375,1)   
            foreground_color: (0, 0, 0, 1)    
            pos_hint: {'x': 0.3, 'y': 0.52}   
            size_hint: (0.675, 0.1)   
            font_size: (canta_kapasitesi_input.width + canta_kapasitesi_input.height) / 24 


        Button:
            id: urunalma_ekraninayonlendirme  
            text: 'Devam'  
            pos_hint: {'x': 0.66, 'y': 0.2}
            size_hint: (0.3, 0.1)    
            background_color: (0.41015625,0.54296875,0.41015625,1)
            color: (0, 0, 0, 1)    
            font_size: (ekran_temizle.width + ekran_temizle.height) / 12 
            bold : True
            on_release:
                root.manager.current = 'Ürün Alma Ekranı' 

        Button:
            id: ekran_temizle
            text: 'Ekranı Temizle'
            pos_hint: {'x': 0.32, 'y': 0.2}
            size_hint: (0.3, 0.1)    
            background_color: (0.41015625,0.54296875,0.41015625,1)
            color: (0, 0, 0, 1)    
            font_size: (ekran_temizle.width + ekran_temizle.height) / 12 
            bold : True
            on_press:   
                root.Ekranı_Temizle()


       """)



class GirisEkrani(Screen):

    def Ekranı_Temizle(self):
        self.manager.ids.GirisEkrani.ids.urun_kapasitesi_input.text = ''
        self.manager.ids.GirisEkrani.ids.canta_kapasitesi_input.text = ''


class UrunAlmaEkrani(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.urun_kapasiteleri = {}
        self.urun_isimleri = {}
        self.urun_degerleri = {}
        self.urun_degerleri_dizi = []
        self.urun_degerleri1_dizi = []
        self.urun_isimleri_dizi = []
        self.urun_isimleri1_dizi = []
        self.urun_kapasiteleri_dizi = []
        self.urun_kapasiteleri1_dizi = []
        self.urun_kapasiteleri2_dizi = []
        self.urun_kapasiteleri3_dizi = []
        self.urun_agirlikdegerleri = []
        self.urun_agirlikdegerleri1 = []
        self.urun_agirlikdegerleri2 = []
        self.son_degerler = []
        self.son_urunisimleri = []
        self.son_kapasiteler = []
        self.greddy_sonuc = 0

    def Tekrar_Hesapla(self, intance):
        self.clear_widgets()
        self.manager.current = 'Giriş Ekranı'

    def Dinamik_Hesapla(self, intance):
        for i in range(int(self.urun_adeti4)):
            self.urun_degerleri1_dizi.append(int(self.urun_degerleri["input_urundegerleri{0}".format(i + 1)].text))
            self.urun_kapasiteleri3_dizi.append(int(self.urun_kapasiteleri["input_urunkapasitesi{0}".format(i + 1)].text))
            self.urun_isimleri1_dizi.append(self.urun_isimleri["input_urunisimleri{0}".format(i + 1)].text)

        self.degerler = []
        for i in range(int(self.urun_adeti4)):
            i = dinamik_algoritma.KnapsackDeger(str(self.urun_isimleri1_dizi[i]), int(self.urun_kapasiteleri3_dizi[i]),int(self.urun_degerleri1_dizi[i]))
            self.degerler.append(i)
        self.baglanti = dinamik_algoritma.Knapsack(int(self.canta_kapasitesi4))
        self.baglanti.DegerlerEkle(self.degerler)
        self.urun_listesi = self.baglanti.Urun_isimleri()
        self.dinamik_sonuc = self.baglanti.Dinamik_Sonuc()

        self.clear_widgets()
        self.y = 35
        self.y_pos = 0
        self.add_widget(Label(text="Alınması Gereken Ürünlerin İsimleri,Kapasiteleri ve Değerleri Yukarıdaki Gibidir..",pos=(0, -270), bold=True, font_size=24, color=(0.41015625, 0.54296875, 0.41015625, 1)))
        self.add_widget(Label(text="Dinamik Algoritma için çıkan sonuç :{}".format(int(self.dinamik_sonuc[-1][-1])), pos=(0, -300),font_size=24, bold=True, color=(0.41015625, 0.54296875, 0.41015625, 1)))
        self.buton3 = Button(text='Tekrar Hesapla', pos=(1020, -20), size_hint=(0.2, 0.05),background_color=(0.41015625, 0.54296875, 0.41015625, 1), bold=True, color=(0, 0, 0, 1))
        self.buton3.bind(on_press=self.Tekrar_Hesapla)
        self.add_widget(self.buton3)

        for i in range(len(self.urun_listesi)):
            self.add_widget(Label(text=str(self.urun_listesi[i]), pos=(50, self.y_pos), font_size=24, bold=True,color=(0.41015625, 0.54296875, 0.41015625, 1)))
            self.y_pos = self.y_pos + self.y

        for i in range(len(self.urun_degerleri1_dizi)):
            self.urun_degerleri1_dizi.remove(self.urun_degerleri1_dizi[0])
            self.urun_kapasiteleri3_dizi.remove(self.urun_kapasiteleri3_dizi[0])
            self.urun_isimleri1_dizi.remove(self.urun_isimleri1_dizi[0])

    def Greddy_Hesapla(self, intance):

        for i in range(int(self.urun_adeti1)):
            self.urun_degerleri_dizi.append(int(self.urun_degerleri["input_urundegerleri{0}".format(i + 1)].text))
            self.urun_kapasiteleri_dizi.append(int(self.urun_kapasiteleri["input_urunkapasitesi{0}".format(i + 1)].text))
            self.urun_kapasiteleri1_dizi.append(int(self.urun_kapasiteleri["input_urunkapasitesi{0}".format(i + 1)].text))
            self.urun_kapasiteleri2_dizi.append(int(self.urun_kapasiteleri["input_urunkapasitesi{0}".format(i + 1)].text))
            self.urun_isimleri_dizi.append(self.urun_isimleri["input_urunisimleri{0}".format(i + 1)].text)

        self.urun_agirlikdegerleri = greddy_agirlik.Agirlik_Degerleri_Hesapla(self.urun_degerleri_dizi,self.urun_kapasiteleri_dizi,self.urun_adeti1)
        self.urun_agirlikdegerleri1 = greddy_agirlik.Agirlik_Degerleri_Hesapla(self.urun_degerleri_dizi,self.urun_kapasiteleri_dizi,self.urun_adeti1)
        self.urun_agirlikdegerleri2 = greddy_agirlik.Agirlik_Degerleri_Hesapla(self.urun_degerleri_dizi,self.urun_kapasiteleri_dizi,self.urun_adeti1)
        self.son_degerler = greddy_deger.Greedy_Algoritmasi_Deger(int(self.canta_kapasitesi1), self.urun_degerleri_dizi,self.urun_kapasiteleri_dizi,self.urun_agirlikdegerleri, int(self.urun_adeti1))
        self.son_urunisimleri = greddy_isim.Greedy_Algoritmasi_İsim(int(self.canta_kapasitesi2),self.urun_isimleri_dizi,self.urun_kapasiteleri1_dizi,self.urun_agirlikdegerleri1, int(self.urun_adeti2))
        self.son_kapasiteler = greddy_kapasite.Greedy_Algoritmasi_Kapasite(int(self.canta_kapasitesi3),self.urun_kapasiteleri2_dizi,self.urun_agirlikdegerleri2,int(self.urun_adeti3))
        self.greddy_sonuc = greddy_sonuc.Sonuc_Hesapla(self.son_degerler)

        self.clear_widgets()
        self.y = 35
        self.y_pos = 0
        self.add_widget(Label(text="Alınması Gereken Ürünlerin İsimleri,Kapasiteleri ve Değerleri Yukarıdaki Gibidir..",pos=(0, -270), bold=True, font_size=24, color=(0.41015625, 0.54296875, 0.41015625, 1)))
        self.add_widget(Label(text="Greed Algoritması için çıkan sonuç :{}".format(self.greddy_sonuc), pos=(0, -300), font_size=24,bold=True, color=(0.41015625, 0.54296875, 0.41015625, 1)))
        self.buton2 = Button(text='Tekrar Hesapla', pos=(1020, -20), size_hint=(0.2, 0.05), bold=True,background_color=(0.41015625, 0.54296875, 0.41015625, 1), color=(0, 0, 0, 1))
        self.buton2.bind(on_press=self.Tekrar_Hesapla)
        self.add_widget(self.buton2)

        for i in range(len(self.son_kapasiteler)):
            self.add_widget(Label(text="Ürün İsmi : {}     Ürün Kapasitesi : {}      Ürün Değeri : {}".format(self.son_urunisimleri[i],self.son_kapasiteler[i],self.son_degerler[i]),pos=(50, self.y_pos), bold=True, font_size=24, color=(0.41015625, 0.54296875, 0.41015625, 1)))
            self.y_pos = self.y_pos + self.y

    def on_enter(self, *args):
        x = -580
        x1 = -170
        x2 = 240
        y = 350
        artan_y = 40
        artan_x = 30
        self.clear_widgets()
        self.urun_adeti1 = self.manager.ids.GirisEkrani.ids.urun_kapasitesi_input.text
        self.urun_adeti2 = self.manager.ids.GirisEkrani.ids.urun_kapasitesi_input.text
        self.urun_adeti3 = self.manager.ids.GirisEkrani.ids.urun_kapasitesi_input.text
        self.urun_adeti4 = self.manager.ids.GirisEkrani.ids.urun_kapasitesi_input.text
        self.canta_kapasitesi1 = self.manager.ids.GirisEkrani.ids.canta_kapasitesi_input.text
        self.canta_kapasitesi2 = self.manager.ids.GirisEkrani.ids.canta_kapasitesi_input.text
        self.canta_kapasitesi3 = self.manager.ids.GirisEkrani.ids.canta_kapasitesi_input.text
        self.canta_kapasitesi4 = self.manager.ids.GirisEkrani.ids.canta_kapasitesi_input.text
        self.buton = Button(text='Greddy Değeri Hesapla', pos=(100, 10), size_hint=(0.2, 0.05), bold=True,background_color=(0.41015625, 0.54296875, 0.41015625, 1), color=(0, 0, 0, 1))
        self.buton.bind(on_press=self.Greddy_Hesapla)
        self.add_widget(self.buton)
        self.buton1 = Button(text='Dinamik Algoritma Değeri Hesapla', pos=(500, 10), bold=True, size_hint=(0.2, 0.05),background_color=(0.41015625, 0.54296875, 0.41015625, 1), color=(0, 0, 0, 1))
        self.buton1.bind(on_press=self.Dinamik_Hesapla)
        self.add_widget(self.buton1)
        self.buton2 = Button(text='Geri', pos=(900, 10), size_hint=(0.2, 0.05), bold=True,background_color=(0.41015625, 0.54296875, 0.41015625, 1), color=(0, 0, 0, 1))
        self.buton2.bind(on_press=self.Tekrar_Hesapla)
        self.add_widget(self.buton2)
        for i in range(int(self.urun_adeti1)):
            self.label_txt = "{0}. Ürün İsmi ".format(i + 1);
            self.label_txt1 = "{0}. Ürün Kapasitesi ".format(i + 1);
            self.label_txt2 = "{0}. Ürün Değeri ".format(i + 1);
            self.input_id = "{0}_urun_ismi".format(i + 1)
            self.input1_id = "{0}_urun_kapasitesi".format(i + 1)
            self.input2_id = "{0}_urun_degeri".format(i + 1)
            self.label = Label(text=self.label_txt, pos=(x, y - artan_y), id=self.label_txt, bold=True,color=(0.41015625, 0.54296875, 0.41015625, 1))
            self.label1 = Label(text=self.label_txt1, pos=(x1 + artan_x, y - artan_y), id=self.label_txt1, bold=True,color=(0.41015625, 0.54296875, 0.41015625, 1))
            self.label2 = Label(text=self.label_txt2, pos=(x2 + artan_x, y - artan_y), id=self.label_txt2, bold=True,color=(0.41015625, 0.54296875, 0.41015625, 1))
            self.urun_isimleri["input_urunisimleri{0}".format(i + 1)] = TextInput(pos=(x + 720, y + 313 - artan_y),id=self.input_id,size_hint=(0.2, 0.06),background_color=(0.37109375, 0.37109375, 0.37109375,1), foreground_color=(0, 0, 0, 1))
            self.urun_kapasiteleri["input_urunkapasitesi{0}".format(i + 1)] = TextInput(pos=(x1 + 750, y + 313 - artan_y), id=self.input1_id, size_hint=(0.2, 0.06),background_color=(0.37109375, 0.37109375, 0.37109375, 1), foreground_color=(0, 0, 0, 1))
            self.urun_degerleri["input_urundegerleri{0}".format(i + 1)] = TextInput(pos=(x2 + 750, y + 313 - artan_y),id=self.input2_id,size_hint=(0.2, 0.06),background_color=(0.37109375, 0.37109375, 0.37109375,1), foreground_color=(0, 0, 0, 1))
            self.add_widget(self.urun_degerleri["input_urundegerleri{0}".format(i + 1)])
            self.add_widget(self.urun_kapasiteleri["input_urunkapasitesi{0}".format(i + 1)])
            self.add_widget(self.urun_isimleri["input_urunisimleri{0}".format(i + 1)])
            self.add_widget(self.label)
            self.add_widget(self.label1)
            self.add_widget(self.label2)
            y = y - artan_y


class EkranYonetimi(ScreenManager):
    pass


class Projem(App):
    def build(self):
        return EkranYonetimi()


if __name__ == '__main__':
    Projem().run()
