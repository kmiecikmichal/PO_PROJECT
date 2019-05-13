import random  
from urllib.request import urlopen
from bs4 import BeautifulSoup

adresurl = input("Wprowadź adres strony internetowej: \nhttp://")

url = "http://" + adresurl
html = urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
#dodać wyjątek w razie braku strony 

text = soup.body.get_text()
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
#dodać coś że nazwa własna to to co wystąpi w kilku językach na raz
#coś z set(inter_pol) & set(inter_eng)

if   len(inter_pol) > len(inter_eng) and len(inter_pol) > len(inter_fra) and len(inter_pol) > len(inter_ger) and len(inter_pol) > len(inter_ita) and len(inter_pol) > len(inter_esp):
     print("Język polski")

elif len(inter_eng) > len(inter_pol) and len(inter_eng) > len(inter_fra) and len(inter_eng) > len(inter_ger) and len(inter_eng) > len(inter_ita) and len(inter_eng) > len(inter_esp):
     print("Język angielski")

elif len(inter_fra) > len(inter_pol) and len(inter_fra) > len(inter_eng) and len(inter_fra) > len(inter_ger) and len(inter_fra) > len(inter_ita) and len(inter_fra) > len(inter_esp):
     print("Język francuski")

elif len(inter_ger) > len(inter_pol) and len(inter_ger) > len(inter_eng) and len(inter_ger) > len(inter_fra) and len(inter_ger) > len(inter_ita) and len(inter_ger) > len(inter_esp):
     print("Język niemiecki")

elif len(inter_ita) > len(inter_pol) and len(inter_ita) > len(inter_eng) and len(inter_ita) > len(inter_fra) and len(inter_ita) > len(inter_ger) and len(inter_ita) > len(inter_esp):
     print("Język włoski")

elif len(inter_esp) > len(inter_pol) and len(inter_esp) > len(inter_eng) and len(inter_esp) > len(inter_fra) and len(inter_esp) > len(inter_ger) and len(inter_esp) > len(inter_ita):
     print("Język hiszpański")

else:
     print("Brak języka w bazie lub niewystarczająca ilość danych")
