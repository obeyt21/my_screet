
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64
import hashlib


window=Tk()
window.title("Title Notes")
window.minsize(width=450, height=700)

logo =Image.open("logo.png")
logo =logo.resize((140, 140))
logo_tk=ImageTk.PhotoImage(logo)
logogoster=tkinter.Label(window, image=logo_tk)
logogoster.pack(pady=(0,20))

baslik=tkinter.Label(text="Başlığı Giriniz..")
baslik.config(font=("Arial", 16, "bold"), pady=10)
baslik.pack()

baslik_deger=tkinter.Entry()
baslik_deger.config(width=25)
baslik_deger.pack()

secret=tkinter.Label(text="Notunuzu Giriniz")
secret.config(font=("Arial", 16, "bold"), pady=10)
secret.pack()

secret_deger=tkinter.Text(width=45, height=20)
secret_deger.pack()

sifre_baslik=tkinter.Label(text="Şifreyi Girin")
sifre_baslik.config(font=("Arial", 16, "bold"), pady=10)
sifre_baslik.pack()

sifre_deger=tkinter.Entry()
sifre_deger.config(width=25)
sifre_deger.pack()

def sifreolustur(sifre):
    key =hashlib.sha256(sifre.encode()).digest()
    return base64.urlsafe_b64encode(key)


def olustur():
    baslik_metni = baslik_deger.get()
    not_metni= secret_deger.get("1.0", END)
    sifre =sifre_deger.get().strip()

    if not sifre:
        print("Şifre boş olamaz. Dosya oluşturulmadı.")
        return

    key =sifreolustur(sifre)
    f =Fernet(key)
    not_encoded =not_metni.encode("utf-8")
    encrypted_note =f.encrypt(not_encoded)

    with open("myscreet.txt", "wb") as dosya:
        dosya.write(f"{baslik_metni.strip().upper()}\n\n".encode("utf-8"))
        dosya.write(encrypted_note)

def sifrecoz():
    sifre =sifre_deger.get().strip()
    encrypted_note=secret_deger.get("1.0", END).strip()

    if not sifre_deger:
        hatamesage.config(text="Şifre boş olamaz. Çözümleme yapılmadı.")
        return
    if not encrypted_note:
        hatamesage.config(text="Lütfen Şifreli Metni Not kısmına girin")
        return
    key =sifreolustur(sifre)
    f =Fernet(key)

    try:
        decrypted_note = f.decrypt(encrypted_note.encode("utf-8")).decode("utf-8")
        secret_deger.delete("1.0", END)
        secret_deger.insert("1.0", decrypted_note)
        hatamesage.config(text="")
    except Exception as e:
        hatamesage.config(text=f"Hatalı Şifre {str(e)}")

kaydet=tkinter.Button(text="Kaydet & Şifrele", command=olustur)
kaydet.pack()

coz =tkinter.Button(text="Çözümle", command=sifrecoz)
coz.pack()

hatamesage=tkinter.Label(text="")
hatamesage.pack()
window.mainloop()