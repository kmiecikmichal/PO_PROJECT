import os
import matplotlib
import matplotlib.pyplot as plt
from tkinter import *
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.request import urlopen
import time as t



def recognition():

    start = t.time()

    try: os.remove("plot.png")
    except: pass
    
    urladdress = e1.get()
    url = "http://" + urladdress

    try: html = urlopen(url).read()
    except URLError:
        l1.place_forget()
        l4.config(text = "Page not found")
        master.minsize(540,274)
        return 


    soup = BeautifulSoup(html,"html.parser")
    text = soup.body.get_text().lower()
    words_txt = text.split()


    with open("PolishBase.txt", encoding="utf8")  as pol:
         words_pol = pol.read().split()

    with open("EnglishBase.txt", encoding="utf8") as eng:
         words_eng = eng.read().split() 

    with open("FrenchBase.txt", encoding="utf8")  as fra:
         words_fra = fra.read().split()

    with open("GermanBase.txt", encoding="utf8")  as ger:
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


    amount = (len(inter_pol) + len(inter_eng) + len(inter_fra) + len(inter_ger) + len(inter_ita) + len(inter_esp))

    if    amount != 0:
          prob_pol = 100 * len(inter_pol) / amount
          prob_eng = 100 * len(inter_eng) / amount
          prob_fra = 100 * len(inter_fra) / amount
          prob_ger = 100 * len(inter_ger) / amount
          prob_ita = 100 * len(inter_ita) / amount
          prob_esp = 100 * len(inter_esp) / amount
          
          try: plt.clf()
          except: pass

          hist_lan = ("POL","ENG","FRA","GER","ITA","ESP")
          hist_val = (prob_pol,prob_eng,prob_fra,prob_ger,prob_ita,prob_esp)

          plt.bar(hist_lan, hist_val)
          plt.title("Probability of language recognition")
          plt.ylim(0, 100)
          plt.ylabel("Probability [%]")
          plt.savefig("plot.png")
        

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

    end = t.time()
    elapsed_time = round((end - start),5)

    try:
        photo = PhotoImage(file = "plot.png")
        l1.config(image = photo)
        l1.image = photo
        l1.place(x = 540, y = 20)
        master.minsize(1200, 520)
    except:
        l1.place_forget()
        master.minsize(540, 274)

    l4.config(text = lang)
    l5.config(text = ("elapsed time ", elapsed_time, "s"))
    
    

master = Tk()
master.minsize(540,274)
master.configure(bg = "gray30")
master.title("Language recognition")


l1 = Label(master)


l2 = Label(master, 
           text  = "Website Address: ", 
           bg    = "gray30", 
           fg    = "white", 
           font  = ("Verdana", 14))
l2.place(x = 20, y = 10, width = 500, height = 64)


e1 = Entry(master,  
           fg    = "gray20", 
           font  = ("Verdana", 14))
e1.place(x = 20, y = 70, width = 500, height = 28)


l3 = Label(master, 
           text  = "Language:", 
           bg    = "gray30", 
           fg    = "white", 
           font  = ("Verdana", 14))
l3.place(x = 20, y = 118, width = 500, height = 64)


l4 = Label(master, 
           text  = "", 
           bg    = "white", 
           fg    = "gray20", 
           font  = ("Verdana",14))
l4.place(x = 20, y = 178, width = 500, height = 28)


l5 = Label(master, 
           text  = "", 
           bg    = "gray30", 
           fg    = "white", 
           font  = ("Verdana",8))
l5.place(x = 20, y = 480, height = 20)


b1 = Button(master, 
            text    = "Quit",
            command = master.quit, 
            bg      = "white", 
            fg      = "gray20", 
            font    = ("Verdana",12))
b1.place(x = 20, y = 226, width = 60, height = 28)


b2 = Button(master, 
            text    = "Recognize", 
            command = recognition, 
            bg      = "white", 
            fg      = "gray20", 
            font    = ("Verdana",12))
b2.place(x = 400, y = 226, width = 120, height = 28)


mainloop( )