# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bioimageit_framework',
    version='0.1.1',
    description='Framework to ease Gui application developement',
    long_description=readme,
    author='Sylvain Prigent',
    author_email='sylvain.prigent@inria.fr',
    url='https://github.com/bioimageit/bioimageit_framework',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "pyside2",
        "qtpy"
    ],
    )
