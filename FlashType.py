import time
from pprint import pprint
import random

f = open('frank.txt', encoding="utf8")
text= f.read()

# making use of the time module -> time elapsed
def timeElapsed(starttime, endtime):
    duration = endtime - starttime

    return duration

# speed calculation at end of each round
def typingSpeed(typedLines, totalTime):

    speed = int(typedLines / (totalTime / 60))

    return speed

# determines and counts errors
def typingErrors(statement, iLine):
    errors = 0
    index = 0
    
    while index < len(iLine):
        if index < len(statement):
            if iLine[index] != statement[index]:
                errors += 1
            
        index += 1
    
    errors += abs(len(statement) - len(iLine))
    
    return errors
# prepares a selected text
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
  
typetext = prepare_text(text)

# generates random line to type
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

# resolve time issues tmr
def main():
    global lines
    totalTime = 0
    typedLines = 0
    totalErrors = 0
    
    
    while totalTime < 120:
        global time
        
        # line = (lines[row]).strip()
        line = sentences(typetext, 10)
        print("Type the following line: '", line, "'")
        
        if totalTime == 0:
            input("press ENTER when you are ready to test :)")
        
        startTime = time.time()
        inputLine = input()
        endTime = time.time()
        
        timePassed = round(timeElapsed(startTime, endTime), 2)
        
        errors = typingErrors(line, inputLine)
        typedLines += len(inputLine.split())
        totalErrors += errors
        print(totalErrors)
        totalTime += timePassed
        print(totalTime)
        
        
    speed = typingSpeed(typedLines, totalTime)
    print("Total Time elapsed : ", int(totalTime), "seconds")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", totalErrors, "errors")
    

        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    