import time

# making use of the time module -> time elapsed
def timeElapsed(stime, etime):
    time = etime - stime

    return time

# speed calculation at end of each round
def typingSpeed(typedLines, totalTime):

    speed = typedLines / totalTime

    return speed

def typingErrors(statement, iLine):

    words = statement.split()
    errors = 0

    for i in range(len(iLine)):
        if i in (0, len(iLine)-1):
            if iLine[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if iLine[i] == words[i]:
                if (iLine[i+1] == words[i+1]) & (iLine[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# resolve time issues tmr
def main():
    global lines
    totalTime = 0
    typedLines = 0
    totalErrors = 0
    row = 0
    
    while totalTime < 120:
        line = lines[row]
        print("Type the following line: '", line, "'")
        
        input("press ENTER when you are ready to test :)")
        
        startTime = time.localtime()
        inputLine = input()
        endTime = time.localtime()
        
        time = round(timeElapsed(startTime, endTime), 2)
        errors = typingErrors(inputLine)
        typedLines += len(inputLine.split())
        totalErrors += errors
        totalTime += time
        row += 1
        
    
    print("Total Time elapsed : ", totalTime, "s")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", totalErrors, "errors")
    
        
if __name__ == '__main__':
    file = open('pride.txt', encoding='utf8')
    text = (file.read())[123:400]
    lines = text.split('\n')

    main()
    
    
    
    
    
    
    