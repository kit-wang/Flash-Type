import time

# making use of the time module -> time elapsed
def timeElapsed(stime, etime):
    time = etime - stime

    return time

# speed calculation at end of each round
def typingSpeed(typedLines, totalTime):

    speed = int(typedLines / (totalTime / 60))

    return speed

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

# resolve time issues tmr
def main():
    global lines
    totalTime = 0
    typedLines = 0
    totalErrors = 0
    row = 0
    
    while totalTime < 120:
        global time
        
        line = (lines[row]).strip()
        print("Type the following line: '", line, "'")
        
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
        row += 1
        
    speed = typingSpeed(typedLines, totalTime)
    print("Total Time elapsed : ", int(totalTime), "seconds")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", totalErrors, "errors")
    
        
if __name__ == '__main__':
    file = open('pride.txt', encoding='utf8')
    text = (file.read())[10000:20000]
    lines = text.split('\n')

    main()
    
    
    
    
    
    
    