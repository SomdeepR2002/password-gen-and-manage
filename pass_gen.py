
import string
import secrets



'''this function will generate a password which is at least 8-12 characters long and super secure
NOT recommended if user wants to remember the passwords, these will be stored locally on the machine'''
def default_password_gen(length=16):
    
    '''instead of generating and checking the password for the conditions we'll create it right from the get go
    using the given conditions'''

    if length < 8:
        raise ValueError("Password length should be at least 8 according to NIST standards")

    #create a string which contains all the possible characters for a password as a reference
    characters = string.ascii_letters + string.digits + string.punctuation

    '''Below mentioned variables store one lowercase,uppercase,numeric and symbolic character each,
    used to adhere to secure password building guidelines i.e makes sure that the password has at least:
        - 1 Lower Case Character
        - 1 Upper Case Character
        - 1 Number
        - 1 Special Character'''

    lower = secrets.choice(string.ascii_lowercase)
    upper = secrets.choice(string.ascii_uppercase)
    numeric = secrets.choice(string.digits)
    symbol = secrets.choice(string.punctuation)
    
    #Building the remaining part of the password
    remaining = ''.join(secrets.choice(characters) for _ in range(12))

    #combining all the parts and shuffling them 
    password = list(upper + lower + remaining + symbol + numeric)
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)
    


print('The password is:',default_password_gen(12))
#def human_readable_password_gen(len,conditions):

s1 = 'suji@231'
s2 = 'ahuh23'
sentence = list(s1 + s2)
print(sentence)
#def check_string(password):

