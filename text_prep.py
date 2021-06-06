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
    new = list(map(str, text.split()))
    l += str(random.choice(new))
    return(l)
print(sentences(bug_text, 10))
