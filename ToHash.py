import hashlib
import random
import time

guess_password = input("Text: ")
guess_passwordf = str(guess_password)

H = hashlib.md5(str(guess_passwordf).encode('utf-8'))

m = hashlib.md5()
line = H.hexdigest()
m.update(str(line).encode('utf-8'))
word_hash = m.hexdigest()

print(word_hash)

time.sleep(5)