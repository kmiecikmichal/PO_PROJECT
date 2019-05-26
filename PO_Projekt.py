import random
from tkinter import *
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.request import urlopen



def recognition():
    
    urladdress = e1.get()
    url = "http://" + urladdress
    try: html = urlopen(url).read()
    except URLError:
        l3.config(text = "Page not found")
        return 
    soup = BeautifulSoup(html,"html.parser")
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
    
    l3.config(text = lang)
  


master = Tk()
master.resizable(0, 0)
master.configure(bg = "gray30")
master.title("Language recognition")


l1 = Label(master, 
           text  = "Website Address: ", 
           bg    = "gray30", 
           fg    = "white", 
           font  = ("Verdana", 14))
l1.pack(pady = 10)


e1 = Entry(master, 
           width = 40, 
           fg    = "gray20", 
           font  = ("Verdana", 14))
e1.pack(padx = 20)


l2 = Label(master, 
           text  = "Language:", 
           bg    = "gray30", 
           fg    = "white", 
           font  = ("Verdana", 14))
l2.pack(pady = 10)


l3 = Label(master, 
           text  = "", 
           width = 40, 
           bg    = "white", 
           fg    = "gray20", 
           font  = ("Verdana",14))
l3.pack(padx = 20)


b1 = Button(master, 
            text    = "Quit",
            command = master.quit, 
            width   = 10,
            bg      = "white", 
            fg      = "gray20", 
            font    = "Verdana")
b1.pack(side = LEFT, padx = 20, pady = 20)


b2 = Button(master, 
            text    = "Recognize", 
            command = recognition, 
            width   = 10,
            bg      = "white", 
            fg      = "gray20", 
            font    = "Verdana")
b2.pack(side = RIGHT, padx = 20, pady = 20)


mainloop( )