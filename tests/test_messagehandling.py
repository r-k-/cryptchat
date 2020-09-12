"""
Test message handling functions.

"""
from ..cryptedcommunication.messagehandling import msg_decrypt, msg_crypt


def test_messages(sample_key):
    msg = b'A message for encryption'
    assert msg == msg_decrypt(sample_key, msg_crypt(sample_key, msg))
