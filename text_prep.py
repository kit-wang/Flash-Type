from pprint import pprint
import random

f = open('frankenstein.txt', encoding="utf8")
text= f.read()

def prepare_text(book):
    t = str(book)
    start = t.find('***') + 3
    d = t[start:]
    start1 = d.find('***') + 3
    end = d.find('*** END OF THE PROJECT')
    t = d[start1:end]
    
    s = t.split()
    s = ' '.join(s)
    final = ""
    
    for letter in s:
        
        if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z') or letter == " ":
            final += letter
    return final
  
print (prepare_text(text))

def sentences(text, count):
    new = []
    l = []
    i = 0
    new = list(map(str, text.split()))
    while i < random.randrange(count):
        l += [random.choice(new)]
        i += 1
    l = ' '.join(l) 
    return(l)
print(sentences(text, 10))
