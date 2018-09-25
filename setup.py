#!/usr/bin/env python3
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='django-pymssql',
    version='2.1.0.0',
    description='Django backend for Microsoft SQL Server using pymssql',
    license='BSD',
    packages=['django_pymssql'],
    install_requires=[
        'Django>=2.1.0,<2.2',
        'pymssql>=2.1',
    ],
    classifiers=CLASSIFIERS,
    keywords='pymssql django',
)
