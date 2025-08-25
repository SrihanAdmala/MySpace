import random

words = ["fruit", "tiger", "quiet", "watch", "beast", "house", "track"]
letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
correctword = random.choice(words)
emptyword = "-" * len(correctword)
isrunning = True
ug = None
guessedletters = []
wroguesses = 0

while isrunning:
    if wroguesses < 6:
        ug = input("Enter a letter: ").lower()
        
        #print(f"length of word ug: {len(ug)}")
        

        if(len(ug) != 1 or ug not in letters):
            print("Please eneter a valid letter.")
            continue

        elif ug in guessedletters:
            print("You already guessed that letter!")
            continue
        
        guessedletters.append(ug)
        
        if ug in correctword:
            print("Good guess!")
            #rw = [i for i, char in enumerate(correctword) if char == ug]
            emptylist = list(emptyword)
            #print(f"emptylist: {emptylist}")
            for j, char in enumerate(correctword):
                if char == ug:
                    emptylist[j] = ug
            emptyword = "".join(emptylist)
            print(emptyword)
            print("\n")

        else:
            wroguesses += 1
            print("Wrong guess!")
            print(emptyword)
            print("You have made", wroguesses, "wrong guesses...")
            print("\n")
            #print(f"wrong guess: {list(emptyword)}")
            #print(f"good guess is: {list(correctword)}")
    
    if "-" not in emptyword:
        print("You guessed the word! Good job!")
        print(f"You made {wroguesses} wrong guesses.")
        isrunning = False
        break
    
    elif wroguesses >= 6:
        isrunning = False
        print("Sorry you lost! Try again!")
        print(f"The word was {correctword} ")