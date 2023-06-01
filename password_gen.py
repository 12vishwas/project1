import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    print("available characters: ",characters)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated Password:", password)
