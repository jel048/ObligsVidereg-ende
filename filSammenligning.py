def main():

    filename1 = 'textone.txt' 
    filename2 = 'texttwo.txt' 
    
    file1Count = getUniqueWordCount(filename1) #Dictionary viser count for hvert unike ord
    file2Count = getUniqueWordCount(filename2)
    
    file1Set = set([key for key in file1Count]) #Omgjør nøkkel i dict til et set med alle unike ord i 
    file2Set = set([key for key in file2Count]) #tekstfilene
    
    valg = showMenu()
    
    while valg > 0 and valg < 7:
        if valg == 1:
            #Printe word count:
            print("FIL 1: ")
            printWordCount(file1Count)
            print("FIL 2:")
            printWordCount(file2Count)
            valg = showMenu()
        
        elif valg == 2:
            #Vise alle unike ord i begge filer
            print("FIL 1:")
            print(file1Set)
            print("FIL 2")
            print(file2Set)
            valg = showMenu()
        elif valg == 3:
            #Vise alle unike ord som forekommer i både første og andre fil(felles ord)
            intersect = file1Set.intersection(file2Set)
            print(intersect)
            valg = showMenu()
        elif valg == 4:
            #Viser alle unike ord som forekommer i første fil, men ikke i andre
            diff1 = file1Set.difference(file2Set)
            print(diff1)
            valg = showMenu()
        
        elif valg == 5:
            #Viser alle unike ord som forekommer i andre fil, men ikke i første:
            diff2 = file2Set.difference(file1Set)
            print(diff2)
            valg = showMenu()
        elif valg == 6:
            #Viser alle unike ord som forekommer enten i første eller i andre fil, bortsett fra felles ord
            symmDiff = file1Set.symmetric_difference(file2Set)
            print(symmDiff)
            valg = showMenu()
        
            
            
        
    
    
        
def getUniqueWordCount(filename):
    wordCounts = {}
    inputFile = open(filename, "r")
    for line in inputFile:
        processLine(line.lower(), wordCounts)
    inputFile.close()
    return wordCounts

def processLine(line, wordCounts): 
    line = replacePunctuation(line) # Replace punctuation with space
    words = line.split() # Get words from each line
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1 # Increase count for word
        else:
            wordCounts[word] = 1 # Add an item in the dictionary


def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")

    return line

def printWordCount(dict):
    for key, value in dict.items():
        print(f'{key + ":":<15} {value} {"ocurrence" if value ==1 else "ocurrences"}')
    
def showMenu():
    print("1 - Vis antall unike ord i begge filer")
    print("2 - Vis alle unike ord i begge filer")
    print("3 - Vis alle unike ord som forekommer både i første og andre fil(felles ord")
    print("4 - Vis alle unike ord som forekommer i første fil, men ikke i andre")
    print("5 - Viser alle unike ord som forekommer i andre fil, men ikke i første")
    print("6 - Viser alle unike ord som forekommer enten i første eller i andre fil, bortsett fra felles ord")   
    print("7 - Avslutt")
    choice = int(input("Skriv inn ditt valg, 1-7: "))  
    return choice
main()