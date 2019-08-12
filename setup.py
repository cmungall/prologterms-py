#from distutils.core import setup
from setuptools import setup

import prologterms

pt_classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

setup(
    name = "prologterms",
    #packages = ["prologterms"],
    py_modules=["prologterms"],
    version = prologterms.__version__,
    description = "A simple python library for generating prolog terms",
    long_description=open("README.rst").read(),
    author = "Chris Mungall",
    author_email = "cmungall+github@gmail.com",
    url = "https://github.com/cmungall/prologterms-py",
    license = "BSD3",
    #tests_require = ["pytest"],
    keywords = ["prolog", "swipl", "swi-prolog", "logic programming", "pengines"],
    classifiers = pt_classifiers,
)
