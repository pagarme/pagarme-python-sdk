# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
else:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='pagarmeapisdk',
    version='6.2.0',
    description='Pagarme API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Pagar.me Pagamentos S/A',
    author_email='suporte@pagar.me',
    url='https://github.com/pagarme/',
    packages=find_packages(),
    install_requires=[
        'jsonpickle~=1.4, >= 1.4.1',
        'requests~=2.24',
        'cachecontrol~=0.12.6',
        'python-dateutil~=2.8.1',
        'enum34~=1.1, >=1.1.10'
    ]
)