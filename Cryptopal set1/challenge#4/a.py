
def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b



def score(s):
	score=0

#defining scores for each alphabats

	freq = {
    'a': 12,
    'b': 13,
    'c': 14,
    'd': 15,
    'e': 16,
    'f': 17,
    'g': 18,
    'h': 19,
    'i': 20,
    'j': 21,
    'k': 22,
    'l': 23,
    'm': 24,
    'n': 25,
    'o': 26,
    'p': 27,
    'q': 28,
    'r': 29,
    's': 30,
    't': 31,
    'u': 32,
    'v': 33,
    'w': 34,
    'x': 35,
    'y': 36,
    'z': 37,
    ' ': 38 }


	for c in s.lower():
		if c in freq:
			score += freq[c]


	return score




maxscore = None
text = None
key = None

for line in open("4.txt", "r"):
    line = line.rstrip()

    b1 = bytearray.fromhex(line)

    for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(b1, b2))
        tempscore = score(plaintext)

        if tempscore > maxscore or not maxscore:
            maxscore = tempscore
            text = plaintext
            key = chr(i)
    print key, text



