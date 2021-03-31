#!/usr/bin/python3

import pathlib
import time 

from cryptography.fernet import Fernet

file = pathlib.Path("message.txt")

if file.exists():
  print("Message exists, loading")
  with open('message.txt', 'r') as my_text:
      msg = my_text.read()
else:
  msg = "This is my test message"

print("My message: ",msg)
msg = msg.encode()

file = pathlib.Path("secret.key")

if not file.exists ():

  print("Key missing, generating")

  # Use Fernet to generate the key file.
  key = Fernet.generate_key() 
  # Store the file to disk to be accessed for en/de:crypting later.
  with open('secret.key', 'wb') as new_key_file:
      new_key_file.write(key)
else:
  print("Key exists, loading")
  # Load the private key from a file.
  with open('secret.key', 'rb') as my_private_key:
      key = my_private_key.read()

print("My key: ",key)

# Instantiate the object with your key.
f = Fernet(key)
# Pass your bytes type message into encrypt.
ciphertext = f.encrypt(msg)
print("Cipher text: ", ciphertext)

# age message for testing
time.sleep(5)
#time.sleep(10)
#print(f.datetime)

# Decrypt the message if less than 8 seconds old.
# If expired, gives cryptography.fernet.InvalidToken
cleartext = f.decrypt(ciphertext,8)
# Decode the bytes back into a string.
cleartext = cleartext.decode()

print("Decrypted text:", cleartext)

