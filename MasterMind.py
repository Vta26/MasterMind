#I want to make an interactable MasterMind Game
#Premise is simple:
#A random 4 letter word or color combination (out of n colors) is provided
#User gueses combination, code informs is any are in the right place, or exist in the correct sequence, but not which ones
#Game continues until user can guess it

import random

def ResponseSort(response):
    for i in range(len(response)-1):
        marker = len(response)-1
        count = 0
        while(marker>=i):
            if count > 100:
                print("error")
                return response
            count += 1
            if response[i] == "•" and response[marker] != "•":
                temp = response[marker]
                response[marker] = response[i]
                response[i] = temp
            elif response[i] == "X" and response[marker] == "O":
                temp = response[marker]
                response[marker] = response[i]
                response[i] = temp
            marker -= 1
    return response
            

def MasterMind():
    playagain = "Y"
    while playagain == "Y":
        guessnumber = 0
        canceled = False
        choice = input("Please select Colors/Words/Numbers -> ").upper()
        category = None
        NotType = False
        while choice != "COLORS" and choice != "WORDS" and choice != "NUMBERS":
            choice = input("Please type Colors, Words, or Numbers -> ").upper()
        if choice == "COLORS":
            colors = ["RED","GREEN","BLUE","YELLOW","ORANGE","PINK","GREY","WHITE"]
            answer = [colors[random.randint(0,7)] for i in range(4)]
            #answer = ['RED', 'YELLOW', 'GREY', 'GREEN']
            category = "Color"
            
        elif choice == "WORDS":
            alphabet = []
            with open("4-Letter Words.txt", encoding="utf8") as f:
                for k in f:
                    alphabet.append(k.split())
            letter = random.randint(0,len(alphabet)-1)
            answer = alphabet[letter][random.randint(0,len(alphabet[letter])-1)]
            #print(answer)
            category = "Letter"
            
        else:
            answer = [str(random.randint(0,9)) for i in range(4)]
            #print(answer)
            category = "Number"
            
        while guessnumber < 20:
            NotType = False
            match choice:
                case "COLORS":
                    print("Available Colors: " + str(colors))
                    guess = input("Guess #" + str(guessnumber + 1) +" -> ").upper().split()
                    for i in guess:
                        if i not in colors:
                            print("Please guess only available colors\n")
                            NotType = True
                            break
                case "WORDS":
                    guess = list(input("Guess #" + str(guessnumber + 1) +" -> ").upper())
                    for i in guess:
                        if i<"A" or i>"Z":
                            print("Please guess only letters\n")
                            NotType = True
                            break
                case "NUMBERS":
                    guess = list(input("Guess #" + str(guessnumber + 1) +" -> "))
                    for i in guess:
                        if not i.isdigit():
                            print("Please guess only numbers\n")
                            NotType = True
                            break
                case _:
                    print("ERROR")
                    return
            if NotType:
                continue
            if guess[0] == "CANCEL":
                canceled = True
                break
            if len(guess) != 4:
                print("\nPlease guess 4 " + choice.lower())
                continue
            if guess == answer:
                print("Correct!")
                print("Answer was: " + str(answer))
                print("You got the answer in " + str(guessnumber+1) + " guesses!")
                break
            print(guess)
            CorrectGuesses= 0
            CorrectPosition = 0
            response = ["•","•","•","•"]
            for anspos, j in enumerate(answer):
                if j == guess[anspos]:
                    response[anspos] = anspos
            for anspos, k in enumerate(answer):
                if response[anspos] != "•":
                    continue
                for guesspos, i in enumerate(guess):
                    if i == k and guesspos not in response:
                        response[anspos] = guesspos
                        break
            for pos, k in enumerate(response):
                if k != "•":
                    if k == pos:
                        response[pos] = "O"
                        CorrectPosition += 1
                    else:
                        response[pos] = "X"
                        CorrectGuesses += 1
            if CorrectPosition == 4:
                print("Correct!")
                print("Answer was: " + str(answer))
                print("You got the answer in " + str(guessnumber+1) + " guesses!")
                break
            response = ResponseSort(response)
            print("\n" + str(response) + "\n" + str(CorrectPosition) + " Correct Position\n" + str(CorrectGuesses) + " Correct " + category + "\n")
            guessnumber += 1
        if guess == 20: 
            print("Sorry, the correct answer was: " + str(answer) + "\n")
        if canceled:
            continue    
        playagain = input("Play Again? (Y/N) -> ").upper()
        while playagain != "Y" and playagain != "N":
            print("Unrecognized Answer")
            playagain = input("Play Again? (Y/N) -> ").upper()
    print("\nThanks for playing!")

MasterMind()