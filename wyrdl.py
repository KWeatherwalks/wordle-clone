# wyrdl.py

WORD = "SNAKE"

for guess_num in range(1, 7):
    guess = input("Guess a word: ").upper()
    if guess == WORD:
        print("Correct")
        break
    print("Wrong")
