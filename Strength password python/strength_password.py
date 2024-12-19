import re
def password_strength(password):
    
    if len(password )< 8:
        return "password is weak and short"
    if re.search(r'[A-Z]',password) is None:
        return "weak : missing uppercase"
    if re.search(r'[a-z]',password) is None:
        return "weak : missing lowercase"
    if re.search(r'[1-9]',password) is None:
        return "weak : missing the number"
    if re.search(r'[\W__]',password) is None:
        return "weak:special character"
    if len(password)<12:
        return "Medium: password is greater than 12+strong"
    
    return "Strong: My password is strong"
    
password = input("enter the password ")
print(password_strength(password))