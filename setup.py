#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import shutil
import sys
from io import open

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


def make_readme(root_path):
    FILES = ('README.rst',)
    for filename in FILES:
        filepath = os.path.realpath(os.path.join(HERE, filename))
        if os.path.isfile(filepath):
            with open(filepath, mode='r', encoding='utf-8') as f:
                yield f.read()


LONG_DESCRIPTION = "\r\n\r\n----\r\n\r\n".join(make_readme(HERE))


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open('version.py').read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version()

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist bdist_wheel")
    if os.system("twine check dist/*"):
        print("twine check failed. Packages might be outdated.")
        print("Try using `pip install -U twine wheel`.\nExiting.")
        sys.exit()
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('django_dynamic_allowedsites.egg-info')
    sys.exit()

setup(
    name='django-dynamic-allowedsites',
    version='0.2.0',
    author='Keryn Knight && nanuxbe && frankyjquintero',
    author_email='python-package@kerynknight.com',
    description="Dynamic ALLOWED_HOSTS based on the configured django.contrib.sites",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=[],
    py_modules=['allowedsites'],
    include_package_data=True,
    install_requires=[
        'Django>=1.4',
    ],
    test_suite='runtests.runtests',
    zip_safe=False,
    url="https://github.com/frankyjquintero/django-allowedsites",
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
