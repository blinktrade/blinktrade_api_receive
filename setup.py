#!/usr/bin/env python

from setuptools import setup

version = "0.1"

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
  name="blinktrade_api_receive",
  version=version,
  author="Rodrigo Souza",
  packages = [
    "blinktrade_api_receive",
    ],
  entry_points = { 'console_scripts':
                     [
                       'blinktrade_api_receive = blinktrade_api_receive.main:main'
                     ]
  },
  install_requires=REQUIREMENTS,
  author_email='r@blinktrade.com',
  url='https://github.com/blinktrade/blinktrade_api_receive',
  license='http://www.gnu.org/copyleft/gpl.html',
  description='Implements the Blockchain.info api receive'
)
