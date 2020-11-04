import random
import time
import sys
import os
import threading
import base64
import string
import itertools

passlength = 0
loop = 10
times = 0

chrs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
n = 1
password = "abca"
passcrack = 0

print("Enter password: ")
password = input("-->> ")
encodedbytes = base64.b64encode(password.encode("utf-8"))
passwordhash = str(encodedbytes, "utf-8")

print("")
print("Password:", password)
print("Password Hash:", passwordhash)
for c in password:
    passlength+=1
print("Password length:", passlength)
time.sleep(2)

def get_random_string():
  pass


if __name__ == '__main__':
  for _ in iter(int, 1):
    t = threading.Thread(target=get_random_string)
    for xs in itertools.product(chrs, repeat=n):
        randomwordthing = ''.join(xs)
        encodedbytes = base64.b64encode(randomwordthing.encode("utf-8"))
        crackedpasswordhash = str(encodedbytes, "utf-8")
        print("Cracking password:", password, "password hash:", passwordhash, "Random password:", randomwordthing, "Random hash:", crackedpasswordhash)
        times = times + 1
        if randomwordthing == password:
            passcrack = 1
            print("Password was cracked:")
            print("Hash:", passwordhash)
            base64_message = passwordhash
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            print("Password:", message)
            print("Cracked the password after", times, "attempts")
            times = times + 1
            time.sleep(100)
    n = n + 1

    t.start()