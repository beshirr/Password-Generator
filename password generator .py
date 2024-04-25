import random
from string import ascii_letters, digits, punctuation


def password_generator():
    password = ""
    chars = []

    for i in range(8):
        chars.append(random.choice(ascii_letters))

    for i in range(4):
        chars.append(random.choice(digits))

    for i in range(4):
        chars.append(random.choice(punctuation))

    for i in range(16):
        password += random.choice(chars)

    return password


created_password = password_generator()
print(f'Your password is {created_password}')
