import re
import tkinter as tk
def strength_check(password = ""):
    strength = 0
    p_length = len(password)
    #Given below is the list of compulsory conditions to ensure password reliability
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[\W_]', password)

    #with open('10-million-password-list-top-1000000.txt') as file:
    #   common = file.read().splitlines()

    #if any(pattern in password for pattern in common):
    #    return "Password found in list of commonly used passwords"
    
    if p_length >= 8:
        strength += 1
    if p_length >= 11:
        strength += 1
    if p_length >= 14:
        strength += 1
    if p_length >= 16:
        strength +=1

    


    
    
