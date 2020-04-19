#!/usr/bin/env python3.6
import random
import string
print('Type password length!')
size=int(input())
def password(size=size,chars=string.ascii_uppercase+string.digits+string.ascii_lowercase):
    
    return ''.join(random.choice(chars) for _ in range(size))

autopass=password()
# print(password())
print(f"Here is your password: {autopass}")