
a= "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
d = a.decode("hex")


print d

b = bytearray(len(d))
for i in range(len(d)):
	b[i] = d[i] ^ d[i]

print b;

