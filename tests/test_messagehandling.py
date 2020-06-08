"""
Test message handling functions. 

"""
from ..cryptedcommunication.messagehandling import msg_encrypt, msg_decrypt 


def test_messages(key):
    msg = b'A message for encryption'
    assert msg == msg_decrypt(key, msg_encrypt(key, msg))

