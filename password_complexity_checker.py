
import re

password = input("Enter Desired Password :")


def password_checker(password):
    length_score = len(password) >= 8
    uppercase_score = bool(re.search(r'[A-Z]', password))
    lowercase_score = bool(re.search(r'[a-z]', password))
    number_score = bool(re.search(r'[0-9]', password))
    special_char = bool(re.search(r'[!@#$%^&*(),.:{}|<>?~]', password))
    total_score = length_score+uppercase_score+lowercase_score+special_char+number_score

    if total_score == 5:
        return "It is a Strong Password"
    elif total_score >= 3:
        return "I is a Good Password"
    else:
        return "It is a Weak Password"


strength = password_checker(password)
print(f"Password Strength : {strength}")
