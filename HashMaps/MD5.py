# This is simply to learn about the MD5 Hash

"""
MD5 is hash function accepts sequence of bytes and returns 128 bit hash value, 
usually used to check data integrity but has a lot of security issues.

This basically has 3 functions.

1. Encode(): converts the string into bytes to be acceptable by the hash function.
2. digest(): This returns the encoded data in byte format
3. hexdigest(): This returns the encoded data in hexadecimal format



"""

import hashlib

#Now, we will take the string that is to be encodes.
str = input()

#We will byte encode the string entered using encode, so that it can be hashed.
str = str.encode()
#Now, we will pass on the encoded data to the hashlib function so that it can be converted.
result = hashlib.md5(str)

#To get the equivalent hexadecimal value, we get.
print("The hexadecimal equivalent of hash is:\t ",result.hexdigest())
print("The decimal equivalent of the hash:\t",result.digest())