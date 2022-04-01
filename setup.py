#!/usr/bin/env python

from setuptools import setup


setup(name='autoparse',
      version='0.1.1',
      description='Automatic Argument Parser from Signature and Docstring',
      author='Fabian Latorre',
      author_email='latorrefabian@gmail.com',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=['autoparse',],
      install_requires=[
          'docstring-parser',],
     )
