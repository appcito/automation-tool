# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('Appcito/appcito.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "appcito-cli",
    packages = ["Appcito"],
    entry_points = {
        "console_scripts": ['appcito-cli = Appcito.appcito:main']
        },
    version = version,
    description = "Appcito Utility",
    long_description = long_descr,
    author = "Prajith Nair",
    author_email = "prajith@appcito.com",
    url = "",
    install_requires = [
        "boto>=2.34.0",
        "prettytable>=0.7.2"
    ],
    )
