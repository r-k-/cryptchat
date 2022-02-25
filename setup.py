"""
Base setup script for building the module.

"""
from setuptools import setup, find_packages

package_name = r'cryptedcommunication'
package_author = r'r-k-'
package_author_mail = r'r-k-@users.github.com'
package_url = r'https://github.com/r-k-/cryptchat.git'

##############################################################################

requirements_file = r'requirements.in'
setup_requirements_file = r'setup_requirements.in'
tests_requirements_file = r'tests_requirements.in'
with open(requirements_file) as rf:
    requirements = rf.readlines()
with open(setup_requirements_file) as rf:
    setup_requirements = rf.readlines()
with open(tests_requirements_file) as rf:
    tests_requirements = rf.readlines()

version_id_file = r'version_id'

setup(
    name=package_name,
    description='Encrypted communication module',
    author=package_author,
    author_email=package_author_mail,
    url=package_url,
    packages=find_packages(include=[r'cryptedcommunication']),
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=tests_requirements,
    vcversioner={r'version_file': version_id_file, },
    python_requires=">=3.7",
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
