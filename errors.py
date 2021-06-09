#This is for errors in words
def error (orig, typeinput):
    n = 0
    a = 0
    errors = 0
    err = ''
    ti = typeinput.split()
    orig1 = orig.split()
    while n < len(ti):
         if n < len(orig1):
            if ti[n] != orig1[a]:
                errors += 1
                if len(ti[n]) >= len(orig1[n]) + len(orig1[n+1]):
                    a += 1
         n += 1
         a += 1
    errors += abs(len(orig1) - len(ti))
    return errors
 
#This is for percent accuracy base on words total  
def accuracy (orig, Typeinput):
    incorrect = error (orig, Typeinput)
    correct = len(orig.split()) - incorrect
    acc = correct/ len(orig.split()) 
    acc = acc * 100
    return str(acc) + '%'
