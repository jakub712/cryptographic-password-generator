import secrets
import time
import hashlib
import string
import json
import pyperclip

#Random words, Cheers chat gpt#
with open ("words.json", "r") as f:
    data = json.load(f)
#Timer 1#
start1 = time.perf_counter_ns()
#symbols#
symbols = "!@#$%^&*()-_=+"
symbol1 = secrets.choice(symbols)
symbol2 = secrets.choice(symbols)
end1 = time.perf_counter_ns()


#grabbing the time
start2 = time.perf_counter_ns()
#generating a random num#
rand_num = secrets.randbits(1024)
end2 = time.perf_counter_ns()
#user input#
user_input =  input("Write some text to further enchrypt the password! ")
#making randbits and timing into a string#
srandom = str(rand_num) + str(start1) + str(start2) + str(end1) + str(end2)
#combining randbits timing and userinput to a string#
combined = user_input + srandom
#encoding the combo#
encoded = combined.encode()
#hashing it#
hashed = hashlib.sha384(encoded).digest()
#slicing the badboy#
num = int.from_bytes(hashed[:5], "big") %100 +1
#a secure password#
charset = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
word_list = data["words"]
passwordv0 = ''.join (charset[b % len(charset)]for b in hashed [:5])
password = f"{secrets.choice(word_list)}{symbol1}{num}{symbol2}{passwordv0}{secrets.choice(word_list)}"
#printing the password#
print (password)
#copy to clipbored#
copy = input("Copy to clipboard? (y/n): ")
if copy == "y":
    pyperclip.copy(password)
    print("Password has been copied")
else:
    print ("Have a good day. ")