"""
Core functions for messages encryption and decryption.

"""
from pymulticrypt import End2End


def msg_crypt(public_key: bytes, msg: bytes) -> bytes:
    e2e = End2End(public_key=public_key)
    return e2e.encrypt(msg, public_key)


def msg_decrypt(private_key: bytes, msg: bytes) -> bytes:
    e2e = End2End(private_key=private_key)
    return e2e.decrypt(msg, private_key)
