#!/usr/bin/env python
from setuptools import setup, find_packages
import platform
import aj

__requires = list(filter(None, open('requirements.txt').read().splitlines()))
if platform.python_implementation() == 'PyPy':
    __requires.append('git+git://github.com/schmir/gevent@pypy-hacks')
    __requires.append('git+git://github.com/gevent-on-pypy/pypycore ')
else:
    __requires.append('gevent>=1')

setup(
    name='aj',
    version=aj.__version__,
    install_requires=__requires,
    description='Web UI base toolkit',
    author='Eugene Pankov',
    author_email='e@ajenti.org',
    url='http://ajenti.org/',
    packages=find_packages(),
)
