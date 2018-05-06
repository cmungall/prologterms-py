from distutils.core import setup

pt_classifiers = [
    "Development Status :: 5 - Production/Stable",
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
    version = "0.0.1",
    description = "A simple python library for interacting with SWI-Prologs Pengines",
    author = "Chris Mungall",
    author_email = "cmungall+github@gmail.com",
    url = "https://github.com/cmungall/prologterms",
    license = "BSD3",
    tests_require = ["pytest"],
    keywords = ["pengines", "pengine", "prolog", "swipl", "swi-prolog", "logic programming"],
    classifiers = pt_classifiers,
)
