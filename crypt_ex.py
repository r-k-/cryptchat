from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# import binascii


def msg_crypt(key: RSA, msg: str) -> bytes:
	encryptor = PKCS1_OAEP.new(pubKey)
	encrypted = encryptor.encrypt(msg)
	return encrypted
	

def msg_decrypt(key: RSA, msg: bytes) -> str:
	decryptor = PKCS1_OAEP.new(keyPair)
	decrypted = decryptor.decrypt(encrypted)
	return decrypted
	

msg = b'A message for encryption'

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
# pubKeyPEM = pubKey.exportKey()
# print(pubKeyPEM.decode('ascii'))

# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
# privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('ascii'))


encrypted = msg_crypt(keyPair, msg)

# print("Encrypted:", binascii.hexlify(encrypted))

decrypted = msg_decrypt(keyPair, encrypted)
print('Decrypted:', decrypted)
