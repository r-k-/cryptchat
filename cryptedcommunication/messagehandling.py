"""
Core functions for messages encryption and decryption.

"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def msg_crypt(key: RSA, msg: bytes) -> bytes:
    encryptor = PKCS1_OAEP.new(key)
    return encryptor.encrypt(msg)


def msg_decrypt(key: RSA, msg: bytes) -> bytes:
    decryptor = PKCS1_OAEP.new(key)
    return decryptor.decrypt(msg)
