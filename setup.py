"""
Base setup script for building the module.

"""
from distutils.core import setup
from os.path import exists


version_id_file = r'version_id'
version_id = None
if exists(version_id_file):
	with open(version_id_file) as verf:
		version_id = verf.readline().strip()
	
setup(name='cryptedcommunication',
      version='1.0',
      description='Encrypted communication module',
      author='r-k-',
      author_email='r-k-@users.github.com',
      url='https://github.com/r-k-/cryptchat.git',
      packages=[])
