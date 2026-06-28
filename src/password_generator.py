import random 
import string 

def generate_password(length ,uppercase, lowercase, numbers, symbols):   
    characters = "" 
    selected_types = 0

    if uppercase:
        characters += string.ascii_uppercase 
        selected_types += 1  
    if lowercase:
        characters += string.ascii_lowercase 
        selected_types += 1  
    if numbers:
        characters += string.digits
        selected_types += 1  
    if symbols:
        characters += string.punctuation 
        selected_types += 1  
    if selected_types < 2:
        return None     

    password = ''.join(random.choice(characters) for _ in range (length))
    return password