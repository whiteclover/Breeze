from setuptools import setup, find_packages
import sys
from breeze import __version__


setup(
    name = 'Breeze',
    version = __version__,
    author = "Thomas Huang",
    author_email='lyanghwy@gmail.com',
    description = "Chat Service",
    license = "GPL",
    keywords = "Chat Service",
    url='https://github.com/thomashuang/Breeze',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires = ['setuptools'],
    classifiers=(
        "Development Status :: Production/Alpha",
        "License :: GPL",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: Chat"
        )
    )