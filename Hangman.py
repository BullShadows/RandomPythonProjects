# Coding Project 1
import time
import random
import sys
import requests
"""
fundo = str(input("Would you like to multiply, divide, add, or subtract? "))
if fundo == "multiply":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("The answer is: ", num1 * num2)
elif fundo == "divide":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("The answer is: ", num1 / num2)
elif fundo == "add":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("The answer is: ", num1 + num2)
elif fundo == "subtract":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("The answer is: ", num1 - num2)
else:
    print("Please enter a valid operation")
    sys.exit()
# Coding project 2
count = 10
while count > 0:
    print(count)
    count -= 1
    time.sleep(1)
"""
# Coding project 3
def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    
    if response.status_code == 200:
        # The API returns a list of words; take the first one
        word_list = response.json()
        if word_list:
            return word_list[0]
        else:
            return None
    else:
        print("Error fetching word:", response.status_code)
        return None
    
wordx = get_random_word()
hangman_stages = [
    "|------\n|     |\n|\n|\n|",
    "|------\n|     |\n|     O\n|\n|",
    "|------\n|     |\n|     O\n|     |\n|",
    "|------\n|     |\n|     O\n|    -|\n|",
    "|------\n|     |\n|     O\n|    -|-\n|",
    "|------\n|     |\n|     O\n|    -|-\n|    /",
    "|------\n|     |\n|     O\n|    -|-\n|    / \\"
]
wordc=[]
for x in wordx:
    wordc.append(x)
for x in wordc:
    print("_", end = "")
y=0
z=[]
new = []
for x in wordc:
    new.append("_")
while y<7:
    guess = str(input("\nEnter a letter: "))
    z.append(guess)
    for x in range(len(wordc)):
        if wordc[x] == guess:
            new[x]=guess
    if guess not in wordc:
        print(hangman_stages[y])
        print('YOU SUCK AND YOU GOT IT WRONG')
        y+=1
    for g in new:
        print(g, end = "")
    if wordc == new:
        print(" You win")
        sys.exit()
    print("\n You have ", 7-y, " guesses left")
    print("Letters guessed: ", z)
if y==7:
    print("You lose")
    print("The word was: ", wordx)
    sys.exit()