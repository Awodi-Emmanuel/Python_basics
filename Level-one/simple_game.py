# import random

def guess_game(num):
    print('What is your guess?')
    guess_num = input()
    for i in num:
        if num[i]==guess_num:
            print("Your guess is correct")
        else:
            print('guess not match')    
result = guess_game([4,5,6,7]) 
print(result)           