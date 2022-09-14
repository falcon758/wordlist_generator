from itertools import chain, combinations

list = []
names = []
tempNames = []


def allSubsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

def listOfImportantWords():
    print("Enter keyword: ")
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)

def permute(inp):
    index = len(tempNames)

    n = len(inp)
   
    mx = 1 << n
   
    inp = inp.lower()

    tempNames.insert(index, [inp])

    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()
   
        temp = ""
        for i in combination:
            temp += i
            
        if temp not in tempNames[index]:
            tempNames[index].append(temp)

def wordListCreator(list):
    lenNames = len(names)
    
    for i in range(0, lenNames):
        for word in names[i]:
            if word not in list:
                list.append(word)
            
            for j in range(0, lenNames):
                if i == j:
            	     continue

                for anotherWord in names[j]:
                    newWord = word + anotherWord
        	    
                    if newWord not in list:
                        list.append(newWord)

def writeToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)


listOfImportantWords()

while('' in names):
    names.remove('')

print("Creating all possible combinations")

for i in names:
    permute(i)

names=tempNames

wordListCreator(list)

writeToFile(list)
