"""
Core functions for messagges encryption and decryption.

"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def msg_crypt(key: RSA, msg: str) -> bytes:
    encryptor = PKCS1_OAEP.new(key)
    return encryptor.encrypt(msg)


def msg_decrypt(key: RSA, msg: bytes) -> str:
    decryptor = PKCS1_OAEP.new(key)
    return decryptor.decrypt(msg)