# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='starscream-flake8',
    version='0.0.1',

    install_requires=[
        'setuptools',
    ],
    py_modules=['starscream_flake'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'SC0* = starscream_flake:main',
        ],
    },
)
