# -*- coding: utf-8 -*-

# Learn more: https://github.com/scottolivermorgan/tradingBot/readme.rst

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tradingBot',
    version='0.1.0',
    description='Forex trading bot',
    long_description=readme,
    author='Scott Morgan',
    author_email='scottolivermorgan@yahoo.com.com',
    url='https://github.com/scottolivermorgan/tradingBot,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

