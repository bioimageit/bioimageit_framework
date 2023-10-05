# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bioimageit_framework',
    version="0.2.0",
    author="Sylvain Prigent and BioImageIT team",
    author_email="bioimageit@gmail.com",
    description='Framework to ease Gui application developement',
    long_description=readme,
    url='https://github.com/bioimageit/bioimageit_framework',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "pyside2",
        "qtpy"
    ],
    )
