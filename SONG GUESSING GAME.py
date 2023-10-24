#!/usr/bin/env phyton

import random

def main():
    """Start a song guessing game."""
    print("Guess the song! There are 4 song choices available: Heather,What was i made for, I love you so and Dandelions.")
    
    song=[
        "dandelions",
        "i love you so",
        "what was i made for",
        "heather"
    ]
    
        
    x=random.choice(song)
    #print(x)
    guess=None
    
    while x!=guess:
        
        guess=str(input("What is our favourite song?"))
        
        if x== guess:
             print("You guessed {}. Congratulations you got it right!.".format(guess))
             break
        else:
             print("You guessed {}.Unfortunately you got the wrong answer.Please try again!".format(guess))
             
    
    
main()
            
            