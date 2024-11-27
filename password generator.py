import random
import string

def generate_password(length=12):
   
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")
    
   
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

   
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    password += random.choices(all_characters, k=length - 4)

    
    random.shuffle(password)

    return ''.join(password)
