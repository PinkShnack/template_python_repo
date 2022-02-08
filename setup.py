#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists, dirname, realpath
from setuptools import setup, Extension, find_packages
import sys


# temaplte originally by Eoghan O'Connell at
#   https://github.com/PinkShnack/template_python_repo
maintainer = "<YOUR_NAME>"
maintainer_email = "<YOUR_EMAIL>"
description = 'template_repo repository for ...'
name = "template_repo"
year = "2022"
url = '<MY_URL>'
license = "<MY_LICENSE_TYPE>"

sys.path.insert(0, realpath(dirname(__file__))+"/"+name)
from _version import version  # noqa: E402


setup(
    name=name,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    url=url,
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license=license,
    description=description,
    long_description=open('README.md').read() if exists('README.md') else '',
    install_requires=[
        "h5py>=3.0.0",
        "numpy>=1.17.0",
        "scipy>=0.14.0",
        ],
    python_requires=">=3.7",
    keywords=["template"],
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Topic :: Any',
                 'Intended Audience :: Everyone',
                 ],
    platforms=['ALL'],
    )
