import random
import string 
import pyperclip  
def get_password_criteria():
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, include_uppercase, include_numbers, include_symbols
def generate_password(length, include_uppercase, include_numbers, include_symbols):
    character_pool = string.ascii_lowercase  
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation
    if not character_pool:
        raise ValueError("No character types selected for password generation.")
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
def main():
    print("Secure Password Generator")
    try:
        length, include_uppercase, include_numbers, include_symbols = get_password_criteria()
        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"Generated Password: {password}")
        pyperclip.copy(password)
        print("Password copied to clipboard.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

