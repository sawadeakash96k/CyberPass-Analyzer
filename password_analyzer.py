# ==========================================
# Advanced Password Strength Analyzer
# ==========================================

import re
import random
import string
from getpass import getpass
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Common weak passwords list
common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "abc123",
    "welcome"
]

# Function to generate strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to analyze password
def analyze_password(password):

    strength = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters")

    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add numbers")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Add special characters")

    # Common password check
    if password.lower() in common_passwords:
        print(Fore.RED + "\n⚠ WARNING: Common weak password detected!")
        strength = 0

    return strength, suggestions

# Function to estimate crack time
def crack_time(strength):

    if strength <= 2:
        return "Few Seconds"

    elif strength == 3:
        return "Few Hours"

    elif strength == 4:
        return "Several Months"

    else:
        return "Several Years"

# Main Program
print(Fore.CYAN + "\n========== PASSWORD ANALYZER ==========\n")

choice = input("1. Analyze Password\n2. Generate Strong Password\n\nEnter Choice: ")

# Analyze Password
if choice == "1":

    password = getpass("\nEnter Your Password: ")

    strength, suggestions = analyze_password(password)

    print("\n========== RESULT ==========\n")

    # Weak Password
    if strength <= 2:
        print(Fore.RED + "Password Strength: WEAK")

    # Medium Password
    elif strength == 3 or strength == 4:
        print(Fore.YELLOW + "Password Strength: MEDIUM")

    # Strong Password
    else:
        print(Fore.GREEN + "Password Strength: STRONG")

    print(Fore.CYAN + f"\nStrength Score: {strength}/5")

    # Crack Time
    print(Fore.MAGENTA + f"Estimated Crack Time: {crack_time(strength)}")

    # Suggestions
    if suggestions:
        print(Fore.YELLOW + "\nSuggestions:")
        for s in suggestions:
            print("- " + s)

    # Save Report
    with open("password_report.txt", "w") as file:
        file.write("PASSWORD ANALYSIS REPORT\n")
        file.write(f"Strength Score: {strength}/5\n")
        file.write(f"Estimated Crack Time: {crack_time(strength)}\n")

    print(Fore.GREEN + "\nReport Saved Successfully!")

# Generate Password
elif choice == "2":

    strong_password = generate_password()

    print(Fore.GREEN + "\nGenerated Strong Password:")
    print(strong_password)

else:
    print(Fore.RED + "\nInvalid Choice")