
#### Hex string need to first convert into bytes(RAW) then it has to convert into base 64

from binascii import unhexlify, b2a_base64 #librabires 


encode = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d".decode("hex").encode("base64")

print encode


