from Crypto.Cipher import AES

# Original ciphertext and plaintext
ciphertext = bytes.fromhex('20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d')
plaintext = b'Pay Bob 100$'

# Desired plaintext
new_plaintext = b'Pay Bob 500$'

# Extract the IV and intermediate values
iv = ciphertext[:16]
intermediate = [ciphertext[i:i+16] for i in range(16, len(ciphertext), 16)]

# Modify the intermediate value corresponding to the last block of plaintext
last_intermediate = intermediate[-1]
last_plaintext = plaintext[-16:]
new_last_plaintext = new_plaintext[-16:]
new_last_intermediate = bytes([a ^ b ^ c for a, b, c in zip(last_plaintext, new_last_plaintext, last_intermediate)])

# Re-encrypt the modified intermediate value
key = b'0123456789abcdef'
cipher = AES.new(key, AES.MODE_CBC, iv)
new_last_ciphertext = cipher.encrypt(new_last_intermediate)

# Construct the new ciphertext
new_ciphertext = iv + b''.join(intermediate[:-1]) + new_last_ciphertext

print(new_ciphertext.hex())