"""
Test message handling functions. 

"""
try:
    from ..cryptedcommunication.messagehandling import msg_encrypt, msg_decrypt
except:
    from ..cryptchat.cryptedcommunication.messagehandling import msg_encrypt, msg_decrypt


def test_messages(key):
    msg = b'A message for encryption'
    assert msg == msg_decrypt(key, msg_encrypt(key, msg))

