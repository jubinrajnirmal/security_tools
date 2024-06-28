import re
import getpass

def check_length(pwd, min_length=8):
    return len(pwd) >= min_length

def check_uppercase(pwd):
    return bool(re.search(r'[A-Z]', pwd))

def check_lowercase(pwd):
    return bool(re.search(r'[a-z]', pwd))

def check_num(pwd):
    return bool(re.search(r'\d', pwd))

def check_spl(pwd):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd))

def pwd_strength(pwd):
    criteria_met = 0
    if check_length(pwd):
        criteria_met += 1
    if check_uppercase(pwd):
        criteria_met += 1
    if check_lowercase(pwd):
        criteria_met += 1
    if check_num(pwd):
        criteria_met += 1
    if check_spl(pwd):
        criteria_met += 1

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    elif criteria_met ==1:
        strength = "Very Weak"

    return strength, criteria_met

def feedback(pwd):
    strength, criteria_met = pwd_strength(pwd)
    print(f"Password Strength: {strength}")
    if strength < "3":
        print("Please enter something complex and usable")

if __name__ == '__main__':
    pwd = getpass.getpass("Enter the password to check its complexity ---> ")
    feedback(pwd)
