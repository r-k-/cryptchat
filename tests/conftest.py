"""
Pytest fixtures

"""
import pytest
from Crypto.PublicKey import RSA


@pytest.fixture(scope='module')
def sample_key():
    yield RSA.generate(1024)
