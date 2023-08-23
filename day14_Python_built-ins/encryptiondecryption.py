# import base64
#
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
#
# # AES ECB mode without IV
#
# data = '{userId: 405, organizationId : 642}'
# key = 'seoifh802308fh34fh8w0839hr03g29^'  # Must Be 16 char for AES128
#
#
# def encrypt(raw):
#     raw = pad(raw.encode(), 16)
#     cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#     return base64.b64encode(cipher.encrypt(raw))
#
#
# def decrypt(enc):
#     enc = base64.b64decode(enc)
#     cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
#     return unpad(cipher.decrypt(enc), 16)
#
#
# encrypted = encrypt(data)
# print('encrypted ECB Base64:', encrypted.decode("utf-8", "ignore"))
#
# # decrypted = decrypt(encrypted)
# # print('data: ', decrypted.decode("utf-8", "ignore"))

from base64 import b64encode, b64decode

# Import the required modules
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# Define the encryption function
def encrypt_AES_CBC_256(key, message):
    key_bytes = key.encode('utf-8')
    message_bytes = message.encode('utf-8')
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    padded_message = pad(message_bytes, AES.block_size)
    ciphertext_bytes = cipher.encrypt(padded_message)
    ciphertext = b64encode(iv + ciphertext_bytes).decode('utf-8')
    return ciphertext


# Define the decryption function
def decrypt_AES_CBC_256(key, ciphertext):
    key_bytes = key.encode('utf-8')
    ciphertext_bytes = b64decode(ciphertext)
    iv = ciphertext_bytes[:AES.block_size]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    ciphertext_bytes = ciphertext_bytes[AES.block_size:]
    decrypted_bytes = cipher.decrypt(ciphertext_bytes)
    plaintext_bytes = unpad(decrypted_bytes, AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext


# Set the 256-bit key and plaintext message
data = '{userId: 405, organizationId : 642}'
key = 'seoifh802308fh34fh8w0839hr03g29^'  # Must Be 16 char for AES128

# Encrypt the message
encrypted_message = encrypt_AES_CBC_256(key, data)

# Decrypt the message
decrypted_message = decrypt_AES_CBC_256(key, encrypted_message)

# Print the original and decrypted messages
print('Original Message:', data)
print('Encrypted Message:', encrypted_message)
print('Decrypted Message:', decrypted_message)
