from binascii import unhexlify, b2a_base64

f= open ("4.txt", "r")

print f

f1= f.readlines()
for x in f1:
	hexd= x.decode("hex")
	print hexd