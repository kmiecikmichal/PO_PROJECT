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

inter_pol = set(words_pol) & set(words_txt)
inter_eng = set(words_eng) & set(words_txt)
#dodać coś że nazwa własna to to co wystąpi w kilku językach na raz
#coś z set(inter_pol) & set(inter_eng)

if   len(inter_pol) >= 3 and len(inter_pol) > len(inter_eng):
     print("Język polski")
elif 1 <= len(words_pol) < 3 and len(inter_pol) > len(inter_eng):
     print("Prawdopodobnie język polski")
elif len(inter_eng) >= 3 and len(inter_pol) < len(inter_eng):
     print("Język angielski")
elif 1 <= len(inter_eng) < 3 and len(inter_pol) < len(inter_eng):
     print("Prawdopodobnie język angielski")
else:
     print("Brak języka w bazie lub niewystarczająca ilość danych")

#zmienić te ify elsy, coś w razie nazw własnych(brak nazw własnych w bazie?
