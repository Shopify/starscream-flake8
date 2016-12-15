# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='starscream-flake8',
    version='0.0.3',

    install_requires=[
        'setuptools',
        'pep8'
    ],
    py_modules=['starscream_flake'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'SC0* = starscream_flake:main',
        ],
    },
)
