from collections import Counter
from collections import defaultdict

with open("EnglishBase.txt", encoding="utf8") as f:
    words = f.read().split()

word_dict = defaultdict(list)
for word, next_word in zip(words, words[1:]):
    word_dict[word].append(next_word)

for i in range(0,len(word_dict[word])):
    words[i] = "".join(words[i])

UniqW = Counter(words)
s = "\n".join(UniqW.keys())

#write
with open("EnglishBase.txt", "w+", encoding = "utf8") as w:
    w.write(s)
w.close()
#append
"""
with open("EnglishBase.txt", "a+", encoding = "utf8") as w:
    w.write(s)
w.close()
"""
