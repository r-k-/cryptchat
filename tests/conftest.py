"""
Pytest fixtures

Use temp folder for running tests that after completion is deleted.

"""
import pytest
from Crypto.PublicKey import RSA


@pytest.fixture(scope='module')
def sample_key():
    yield RSA.generate(1024)


# @pytest.fixture(scope='module')
# def temp_folder():
#     pass
