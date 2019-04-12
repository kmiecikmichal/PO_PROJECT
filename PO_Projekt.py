import random 

with open("PolishBase.txt", encoding="utf8") as pol:
     words_pol = pol.read().split()

with open("EnglishBase.txt", encoding="utf8") as eng:
     words_eng = eng.read().split()

with open("textfile.txt", encoding="utf8") as txt:
     words_txt = txt.read().split()

inter_pol = set(words_pol) & set(words_txt)
inter_eng = set(words_eng) & set(words_txt)
#dodać coś że nazwa własna to to co wystąpi w kilku językach na raz
#coś z set(inter_pol) & set(inter_eng)

if   len(inter_pol) >= 3 and len(inter_pol) > len(inter_eng):
     print("Język polski")
     print(inter_pol)
elif 1 <= len(words_pol) < 3 and len(inter_pol) > len(inter_eng):
     print("Prawdopodobnie język polski")
elif len(inter_eng) >= 3 and len(inter_pol) < len(inter_eng):
     print("Język angielski")
     print(inter_eng)
elif 1 <= len(inter_eng) < 3 and len(inter_pol) < len(inter_eng):
     print("Prawdopodobnie język angielski")
else:
     print("Brak języka w bazie lub niewystarczająca ilość danych")

#zmienić te ify elsy, coś w razie nazw własnych(brak nazw własnych w bazie?
