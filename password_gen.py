import secrets
import time
import hashlib
import string
import random
import json
import pyperclip

#Random words, Cheers chat gpt#
with open ("words.json", "r") as f:
    data = json.load(f)
#symbols#
symbols = "!@#$%^&*()-_=+"
symbol1 = random.choice(symbols)
symbol2 = random.choice(symbols)

#grabbing the time
start = time.perf_counter_ns()
#generating a random num#
for bits in [128]:
    rand_num = secrets.randbits(bits)
#user input#
user_input =  input("Write some text to further enchrypt the password! ")
#making randbits and timing into a string#
srandom = str(rand_num) + str(start)
#combining randbits timing and userinput to a string#
combined = f"{user_input}{srandom}"
#encoding the combo#
encoded = combined.encode()
#hashing it#
hashed = hashlib.sha384(encoded).digest()
#slicing the badboy#
num = int.from_bytes(hashed[:3], "big") %100 +1
#a secure password#
charset = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
word_list = data["words"]
random.seed(hashed)
password = f"{random.choice(word_list)}{symbol1}{num}{symbol2}{random.choice(word_list)}"
#printing the password#
print (password)
#copy to clipbored#
copy = input("Copy to clipboard? (y/n): ")
if copy == "y":
    import pyperclip
    pyperclip.copy(password)
    print("Password has been copied")
else:
    ("Have a good day. ")