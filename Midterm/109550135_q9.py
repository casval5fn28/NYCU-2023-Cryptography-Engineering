"""Question 9"""
# xor two strings of different lengths
def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
    
cipher = "20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d".split(' ')
# for CBC parts , first one'll be IV
cipherIV = cipher[0]
cipherC0 = cipher[1]
plaintext = "Pay Bob 100$"
plaintext_tgt = "Pay Bob 500$"

# apply paddings
pad_tmp1 = str(len(cipherC0) - len(plaintext))
padding_1 = "".join([pad_tmp1] * int(pad_tmp1))
pad_tmp2 = str(len(cipherC0) - len(plaintext_tgt))
padding_2 = "".join([pad_tmp2] * int(pad_tmp2))
 
plaintext += padding_1
plaintext_tgt += padding_2

# XOR the plaintext
xor_plain = strxor(plaintext, plaintext_tgt)

# xor again with IV
fin_IV = strxor(xor_plain, cipherIV)
print("Q9:")
print ("  Resulting cipher = " , fin_IV + cipher[1])