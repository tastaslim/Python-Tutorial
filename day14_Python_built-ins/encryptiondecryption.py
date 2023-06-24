import base64

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

password = input("Enter encryption password: ")


def get_private_key(pwd):
    salt = b"this is a salt"
    kdf = PBKDF2(pwd, salt, 64, 1000)
    key = kdf[:32]
    return key


def encrypt(raw, pwd):
    private_key = get_private_key(pwd)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(enc, pwd):
    private_key = get_private_key(pwd)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


# First let us encrypt secret message
encrypted = encrypt("This is a secret message", password)
print(encrypted)

# Let us decrypt using our original password
decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))
