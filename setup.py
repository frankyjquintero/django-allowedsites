#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from setuptools import setup


HERE = os.path.abspath(os.path.dirname(__file__))


def make_readme(root_path):
    FILES = ('README.rst', 'LICENSE', 'CHANGELOG', 'CONTRIBUTORS')
    for filename in FILES:
        filepath = os.path.realpath(os.path.join(HERE, filename))
        if os.path.isfile(filepath):
            with open(filepath, mode='r') as f:
                yield f.read()


LONG_DESCRIPTION = "\r\n\r\n----\r\n\r\n".join(make_readme(HERE))

setup(
    name='django-dynamic-allowedsites',
    version='0.2.0',
    author='Keryn Knight && nanuxbe && frankyjquintero',
    author_email='python-package@kerynknight.com',
    description="Dynamic ALLOWED_HOSTS based on the configured django.contrib.sites",
    long_description=LONG_DESCRIPTION,
    packages=[],
    py_modules=['allowedsites'],
    include_package_data=True,
    install_requires=[
        'Django>=1.4',
    ],
    test_suite='runtests.runtests',
    zip_safe=False,
    license="BSD License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
