import random  
from tkinter import * 
from bs4 import BeautifulSoup
from urllib.request import urlopen


def recognition():
    #adresurl = input("Wprowadź adres strony internetowej: \nhttp://") #konsolowe wprowadzanie
    adresurl = e1.get()
    url = "http://" + adresurl
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    #dodać wyjątek w razie braku strony 

    text = soup.body.get_text().lower()
    words_txt = text.split()


    with open("PolishBase.txt", encoding="utf8") as pol:
        words_pol = pol.read().split()

    with open("EnglishBase.txt", encoding="utf8") as eng:
        words_eng = eng.read().split() 

    with open("FrenchBase.txt", encoding="utf8") as fra:
         words_fra = fra.read().split()

    with open("GermanBase.txt", encoding="utf8") as ger:
         words_ger = ger.read().split() 

    with open("ItalianBase.txt", encoding="utf8") as ita:
         words_ita = ita.read().split()

    with open("SpanishBase.txt", encoding="utf8") as esp:
        words_esp = esp.read().split() 


    inter_pol = set(words_pol) & set(words_txt)
    inter_eng = set(words_eng) & set(words_txt)
    inter_fra = set(words_fra) & set(words_txt)
    inter_ger = set(words_ger) & set(words_txt)
    inter_ita = set(words_ita) & set(words_txt)
    inter_esp = set(words_esp) & set(words_txt)


    if   len(inter_pol) > len(inter_eng) and len(inter_pol) > len(inter_fra) and len(inter_pol) > len(inter_ger) and len(inter_pol) > len(inter_ita) and len(inter_pol) > len(inter_esp):
         lang = "Polish language"

    elif len(inter_eng) > len(inter_pol) and len(inter_eng) > len(inter_fra) and len(inter_eng) > len(inter_ger) and len(inter_eng) > len(inter_ita) and len(inter_eng) > len(inter_esp):
         lang = "English language"

    elif len(inter_fra) > len(inter_pol) and len(inter_fra) > len(inter_eng) and len(inter_fra) > len(inter_ger) and len(inter_fra) > len(inter_ita) and len(inter_fra) > len(inter_esp):
         lang = "French language"

    elif len(inter_ger) > len(inter_pol) and len(inter_ger) > len(inter_eng) and len(inter_ger) > len(inter_fra) and len(inter_ger) > len(inter_ita) and len(inter_ger) > len(inter_esp):
         lang = "German language"

    elif len(inter_ita) > len(inter_pol) and len(inter_ita) > len(inter_eng) and len(inter_ita) > len(inter_fra) and len(inter_ita) > len(inter_ger) and len(inter_ita) > len(inter_esp):
         lang = "Italian language"

    elif len(inter_esp) > len(inter_pol) and len(inter_esp) > len(inter_eng) and len(inter_esp) > len(inter_fra) and len(inter_esp) > len(inter_ger) and len(inter_esp) > len(inter_ita):
         lang = "Spanish language"

    else:
         lang = "No language in the database or insufficient data"

    l2.config(text = lang)
  

master = Tk()

l1 = Label(master, text="Website Address: ")
l1.pack()
l2 = Label(master, text = "")
l2.pack()

e1 = Entry(master)
e1.pack()

b1 = Button(master, text='Quit', command = master.quit)
b1.pack()
b2 = Button(master, text='Recognize', command = recognition)
b2.pack()

mainloop( )