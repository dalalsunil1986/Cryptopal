
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










def break_bit_xor(b1):
    maxscore = None
    text = None
    key = None

    for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(b1, b2))
        pscore = score(plaintext)

        if pscore > maxscore or not maxscore:
            maxscore = pscore
            text = plaintext
            key = chr(i)
    return key, text


b1 = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

print break_bit_xor(b1)
