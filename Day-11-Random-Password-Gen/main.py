#Random Password Generator
import random
import string

def generate_password(length):
    # Define the set of characters to choose from
    letters = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters) for i in range(length))
    return password

password = generate_password(8)
print(password)

