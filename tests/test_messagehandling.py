"""
Test message handling functions.

"""
import pytest

from ..cryptedcommunication.messagehandling import msg_decrypt, msg_crypt


@pytest.mark.unit
def test_messages(sample_key):
    msg = r'A message for encryption'
    assert msg == msg_decrypt(sample_key[r'private'],
                              msg_crypt(sample_key[r'public'], msg))
