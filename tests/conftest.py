"""
Pytest fixtures

"""
import pytest
from pymulticrypt import End2End


@pytest.fixture(scope='module')
def sample_key():
    yield End2End().keys()
