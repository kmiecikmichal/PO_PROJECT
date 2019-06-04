from collections import Counter
from collections import defaultdict
import re


with open("ItalianBase.txt", encoding="utf8") as f:
     words = f.read().split(" ")

word_dict = defaultdict(list)
for word, next_word in zip(words, words[1:]):
    word_dict[word].append(next_word)

for i in range(0,len(word_dict[word])):
    words[i] = "".join(words[i])

UniqW = Counter(words)
w = "\n".join(UniqW.keys()).lower() #unikalne znaki, zapis lowercase
s = re.sub("\d+", "", w) #usuwa cyfry
#s = re.sub("«", "", w) #do wpisywania innych znaków do usunięcia » «

#write
with open("ItalianBase.txt", "w+", encoding = "utf8") as w:
    w.write(s)
w.close()

"""
#append
with open("EnglishBase.txt", "a+", encoding = "utf8") as w:
    w.write(s)
w.close()
"""