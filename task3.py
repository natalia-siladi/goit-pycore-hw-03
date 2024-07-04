import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(number):
    
    pattern = r"[^\d]" 
    replacement = ""
    formated_phone = re.sub(pattern, replacement, number)  

    if len(formated_phone)== 12:
            new_phone_number = "+" + formated_phone
            
    elif len(formated_phone) == 11:
            new_phone_number = "+3" + formated_phone
            
    elif  len(formated_phone) == 10:
            new_phone_number = "+38" + formated_phone
            
    return new_phone_number 

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)      
