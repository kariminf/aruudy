import os
from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name = "aruudy",
    version = "0.1.0",
    author = "Abdelkrime Aries",
    author_email = "kariminfo0@gmail.com",
    description = ("Arabic poetry package"),
    license = "Apache-2.0",
    keywords = "arabic nlp languages poetry",
    url = "https://github.com/kariminf/aruudy",
    packages=['aruudy'],
    long_description=long_description
)
