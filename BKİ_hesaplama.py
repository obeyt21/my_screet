import tkinter
from tkinter import *

window =Tk()
window.title("Vucut Kitle İndexi")
window.minsize(width=400, height=300)

my_header=tkinter.Label(text="Vucut Kitle İndexi Hesaplama", font='Arial' 'bold' )
my_header.config(padx=10, pady=10)
my_header.pack()

kilogram=tkinter.Label(text="Kilonuzu Girin")
kilogram.pack()

kilo_deger=tkinter.Entry()
kilo_deger.config(width=8)
kilo_deger.pack()

boy=tkinter.Label(text="Boyunuzu Girin")
boy.pack()

boy_deger=tkinter.Entry()
boy_deger.config(width=8)
boy_deger.pack()


sonuc=tkinter.Label(text="")
sonuc.config(pady=10, padx=10)
sonuc.pack()

sonuc_2=tkinter.Label(text="")
sonuc_2.pack()
def hesapla():
    try:
        kilo = float(kilo_deger.get())
        boy = float(boy_deger.get())
        vki = kilo / boy ** 2
        sonuc.config(text=f"Vucut Kitle İndexsiniz: {vki}")

        if vki < 16.0:
            sonuc_2.config(text="Aşırı Düzeyde Zayıfsınız")
        elif 16.0 <= vki <= 16.99:
            sonuc_2.config(text="Orta Düzeyde Zayıfsınız")
        elif 17.0 <= vki <= 18.49:
            sonuc_2.config(text="Hafif Düzeyde Zayıflık")
        elif 18.49 <= vki <= 18.5:
            sonuc_2.config(text="Zayıfsınız")
        elif 18.5 < vki < 24.99:
            sonuc_2.config(text="Normal Kilolusunuz")
        elif 25.0 <= vki < 30.0:
            sonuc_2.config(text="Hafif Obez")
        elif 30.0 <= vki <= 34.99:
            sonuc_2.config(text="1. Dereceden Obez")
        elif 35.0 <= vki <= 39.99:
            sonuc_2.config(text="2. Dereceden Obez")
        elif 40 <= vki:
            sonuc_2.config(text="3. Dereceden Obez")
    except ValueError:
        sonuc.config(text="Lütfen geçerli sayı girin.")


hesaplabutonu=tkinter.Button(text="Hesapla", command=hesapla)
hesaplabutonu.config(pady=5, padx=3)
hesaplabutonu.pack()

window.mainloop()