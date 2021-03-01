from __future__ import division, print_function

from setuptools import setup, find_packages

VERSION = '0.0.2'

REQUIRED_PACKAGES = [
    'apache-beam>=2.8.0,<3.0.0',
    'requests'
]

REQUIRED_PACKAGES_TEST = [
    'nose>=1.3.7,<2.0.0'
]

REQUIRED_PACKAGES_DOCS = []

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='beam-bc365',
    version=VERSION,
    author='Brendan Kamp',
    author_email='brendankamp757@gmail.com',
    description='Microsoft Business Central transofrm for the Apache beam python SDK.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spazzy757/beam-bc365",
    install_requires=REQUIRED_PACKAGES,
    extras_require={'dev': REQUIRED_PACKAGES_TEST + REQUIRED_PACKAGES_DOCS},
    packages=find_packages(exclude=("test", "tests")),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
