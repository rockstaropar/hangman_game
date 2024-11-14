import random

words = ["algorithm", "function", "variable", "compile", "iterate", "recursion", "binary", "array", "syntax", "pointer"]

while True:
    ran_word1 = random.choice(words)
    check=list(ran_word1)
    ran_word=list(ran_word1)
    ch = []
    for i in range(0,len(ran_word)):
        ch.append("_")
    flag=True
    i=1
    while(flag and i<=7):
        guess=""
        while(True):
            user_input = input("Enter a character: ")
            if len(user_input) == 1 and user_input.isalpha():
                guess=user_input
                break;
            else:
                print("That's not a valid character.")
                
        if(guess in ran_word):
            for j in range(0,len(ran_word)):
                if ran_word[j]==guess :
                    ch[j]=guess
                    ran_word[j]='_'
                    break
            for o in range(0,len(ch)):
                print(ch[o],end="")
            print()
            if ch==check:
                print("YOU GUESSED THE WORD")
                print("Phew… you are saved")
                flag=False
                    
        else:
            print("HANGMAN")
            i+=1
            for k in range(0,i-1):
                print(" ",end="")
            print("^")
            if i==7:
                print("YOU ARE HANGED")
                break
                
            
    play_again = input("Do you want to play again? ").lower()
    
    if play_again != "yes":
        print("Goodbye!")
        break


