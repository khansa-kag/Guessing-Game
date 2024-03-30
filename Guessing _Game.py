#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install streamlit


# In[ ]:


import pandas as pd
import numpy as np 
import streamlit as st
import random


# In[ ]:


secret_number = (random.randint(1, 50))
print(secret_number)
attempt = 5
guess = 0
print("Welcome to 'Number Guessing Game'!")
print("Can you figure out the secret number hidden between 1 and 50?")
print("You have 5 attempts to guess it right.")
print("Enter your guess in the box below and click 'Submit' to see if you've cracked the code")
print("Good luck!")
while attempt > 0:
    try:
        guess = int(st.text_input('Guess a number between 1 and 50:'))
        if guess == secret_number:
            print("Congragulation !")
            break
        elif guess>secret_number:
            print("Your guess is bigger than the secret number")
        else:
            print("Your guess is smaller than the secret number")
        
        attempt-=1
        print(f"Attempts left are: {attempt} ")
       
        if attempt == 0:
            print (f"The game is Over. The secret number was: {secret_number}")
        else: 
            pass
    except:
        print(f"Invalid input! Please enter a valid number. You have {attempt-1} attempts left")
        attempt-=1
#    except:
 #       print(f"Invalid input! Please enter a valid number. You have {guess-1} attempts left")
  #      guess-=1

    
 


