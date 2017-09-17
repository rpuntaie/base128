#! /usr/bin/env python
# vim: fileencoding=utf-8 

#sudo python setup.py bdist_wheel
#twine upload ./dist/base128*.whl

from setuptools import setup
import os

#See 
#https://pypi.python.org/pypi?%3Aaction=list_classifiers
#for classifiers

__version__ = '0.1.0'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

conf = dict(name='base128',
    version = __version__,
    description="Encodes to and decodes from base128.",
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only"
    ],
    keywords=['encoding, base128, iso-8859'],
    author = 'Roland Puntaier',
    author_email = 'roland.puntaier@gmail.com',
    license='MIT',
    url = 'https://github.com/rpuntaie/base128',
    packages=['base128'],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'bitarray>=0.8.1'
    ],
    python_requires='>3.3',
    tests_require=[],
    entry_points={
         'console_scripts': [
         'base128 = base128.__main__:main',
              ]
      },

    )

if __name__ == '__main__':
    setup(**conf)
