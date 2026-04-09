# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:57:01 2026

@author: Abror
"""
import random
from sozlar import words

def get_words():
    word = random.choice(words)
    while "-" in  word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display (user_letters,word):
    display_letters = " "
    for letter in word:
        if letter in user_letters.upper():
            display_letters += letter
        else:
            display_letters += "-"
    return display_letters

def play():
    word = get_words()
    # So'zdagi harflar
    word_letters = set(word)
    #Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f" Men {int(len(word))} xonali so'z o'yladm. Topa olasizmi?")
    #print(word)
    while len(word_letters)>0:
        print(display(user_letters, word))
        if int(len (user_letters))>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            
        
        letter = input("harf kiriting >>> ").upper()
        if letter in user_letters:
            print("bu harfni oldin kiritgansiz. Boshqa harf kiriting >>> ")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri")
        else:
            print("bunday harf yo'q")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini  topdingiz!")
