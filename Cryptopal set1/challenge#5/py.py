def xor(b1, b2):
  b = bytearray(len(b1))
  for i in range(len(b1)):
    b[i] = b1[i] ^ b2[i]
  return b


text = "".join(["Burning 'em, if you ain't quick and nimble\n","I go crazy when I hear a cymbal"])

key = bytearray("ICE" * len(text))

message = bytes(xor(bytearray(text), key))

print message.encode("hex")
