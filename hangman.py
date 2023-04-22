#This is the program to play hangman

def hangman(word):
    wrong=0
    stages=["",
            "______      ",
            "|           ",
            "|     |     ",
            "|     O     ",
            "|    /|\    ",
            "|    / \    ",
            "|           "
            ]

    lista_parola = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages)-1:
        print("\n")
        guess = input("Guess a letter: ")
        if guess in lista_parola:
            guess_index = lista_parola.index(guess)
            board[guess_index] = guess
            lista_parola[guess_index] = "$"
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
              print("You win!")
              print(" ".join(board))
              win=True
              break
    if not win:
        print("You lose! It was: {}".format(word))

hangman("house")        
