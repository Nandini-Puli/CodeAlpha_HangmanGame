import random

word_list=["grapes","guava","mango","papaya","strawberry"]
lives=6
choosen=random.choice(word_list)

display=[]
for i in range(len(choosen)):
    display+= '_'
print(display)  
game_over=False
while not game_over: 
    Guess=input("Guess a Letter:").lower()
    for pos in range(len(choosen)):
        letter=choosen[pos]
        if letter == Guess:
            display[pos]=Guess
    print(display)        
    if Guess not in choosen:
        lives-=1        
        if lives==0:
            game_over=True
            print("You lose!!")
    if '_' not in display:
        game_over=True
        print("You Win!!")        
