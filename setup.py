from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'A simple to use economy module'
LONG_DESCRIPTION = 'Economy module that supports discord, but you could use it where you want! Uses JSON files to store data.'

# Setting up
setup(
    name="pyeconomy",
    version=VERSION,
    author="konradsic (Konrad)",
    author_email="<sicinskikonrad@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['discord'],
    keywords=['python', 'json', 'discord', 'discord-bot', 'cryptocurrency', 'economy'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)