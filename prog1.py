#!/usr/bin/python3

'''

  31 Mar 2021 - gswann

  Example program to use Jake Krajewski's
  Fernet cipher class
   
'''

import FernetCypher as fc

msg = "this is a test message"

print("My message: ", msg)

# create instance of the class object
# if there is no key file, in this folder,
# it will create one
myFernet = fc.FernetCipher()

# our instance has a key either loaded from the file,
# or created
print ("My key: ",myFernet.key)

# Pass your bytes type message into encrypt.

ciphertext = myFernet.encrypt(msg)
print("Cipher text: ",ciphertext)

cleartext = myFernet.decrypt(ciphertext)

# convert to string
cleartext = cleartext.decode()

# print my message
print("Clear text: ",cleartext)
