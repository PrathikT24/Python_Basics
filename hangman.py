import random
stages=['''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words=["apple", "boomer", "cinderella", "cylinder"]
chosen_word=random.choice(words)

lives=6

display=[]
for _ in range(len(chosen_word)):
    display+="_"


end=False
while end==False:

    guess=input("Guess a letter \n ").lower()


    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        #print(f"position: {position} \n letter: {letter} \n guessed letter: {guess}")
        if letter==guess:
            display[position]=letter
    
    if guess not in chosen_word:
        print(f"You guessed wrong you lose a life")
       lives-=1
        if lives==0:
            end=True
            print("You lose ")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end=True
        print("You win \n ")
    print(stages[lives])
