import random
guess = ["_","_","_","_","_"]
ord = []
new = []
guessess = 0
numprinted = []
finalwordlist = [[],[],[],[]]
with open('Word_List.txt','r') as file:
    lines = len(file.readlines())-1
with open('Word_List.txt','r') as file:
    # reading each line    
    for line in file:
        # reading each word        
        for word in line.split("    "):
            new.append(word)
for i in new[random.randint(0,lines)]:
    if i !=" ":
        ord.append(i)
for x in ord:
    if x == "\t" or x == "\n":
        ord.remove(x)
x=-1
for z in ord:
    if z == z.upper():
        x+=1
    finalwordlist[x].append(z.lower())
finalword = []
x =0
while len(numprinted)<len(finalwordlist):
    y = random.randint(0,len(finalwordlist)-1)
    if y not in numprinted:
        numprinted.append(y)
wordnumbercounter = 0
finalword.append(finalwordlist[numprinted[wordnumbercounter]])
print(guess)
play = True
while play == True:
    while guessess < 5 and guess != finalword[0]:
        userin = input("Enter your guess\n-------------------\n")
        #print(finalword)
        digitchecker = False
        for i in userin:
                if i.isdigit() == True:
                    digitchecker = True
                else:
                    digitchecker = False
        while digitchecker == True:
            userin = input("Enter in a 5 letter word no numbers\n-------------------\n")
            for i in userin:
                if i.isdigit() == True:
                    digitchecker = True
                else:
                    digitchecker = False
        while len(userin) != 5:
            userin = input("Enter in a 5 letter word\n-------------------\n")
        for indx,i in enumerate(userin):
            if i in finalword[0] and userin.index(i) == finalword[0].index(i):
                print('\033[92m'+i+'\033[0m',end = "")
                guess[indx] = i
            if i in finalword[0] and userin.index(i) != finalword[0].index(i):
                print('\033[93m'+i+'\033[0m',end="")
            if i not in finalword[0]:
                print('\033[91m'+i+'\033[0m',end="")
        print(guess)
        guessess +=1
        x=0
    if wordnumbercounter>=4:
        print("congrats you got all of them play again for more words")
        break
    if guess == finalword[0]:
        print("Nice you got the word")
        userin = input("Do you want to play again (yes/no)").lower()
    if guess != finalword[0]:
        print(f"The word was {finalword[0]}")
        userin = input("Do you want to play again (yes/no)").lower()
    if userin == "yes":
        play = True
        wordnumbercounter+=1
        guessess = 0
        finalword[0] = finalwordlist[numprinted[wordnumbercounter]]
        guess = ["_","_","_","_","_"]
    else:
        play = False