# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
from codecs import open

import os


# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
# Get the long description from the README file
with open(os.path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()


# Get the relevant setup parameters from the package
parameters = {}
with open(os.path.join(here, 'sarpy_apps', '__about__.py'), 'r') as f:
    exec(f.read(), parameters)


install_requires = ['numpy>=1.9.0', 'sarpy>=1.0.47', 'tk_builder>=1.0.1']
tests_require = []
if sys.version_info[0] < 3:
    tests_require.append('unittest2')
    # unittest2 only for Python2.7, we rely on subTest usage
    install_requires.extend(['typing', 'future'])

setup(name=parameters['__title__'],
      version=parameters['__version__'],
      description=parameters['__summary__'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(exclude=('*tests*', '*examples*')),
      url=parameters['__url__'],
      author=parameters['__author__'],
      author_email=parameters['__email__'],  # The primary POC
      install_requires=install_requires,
      zip_safe=True,
      test_suite="tests",
      tests_require=tests_require,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ],
      platforms=['any'],
      license='MIT'
      )
