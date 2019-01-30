"""
Module installation script
"""
import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')) as f:
    LONG_DESCRIPTION = f.read()


def package_files(directory):
    """
    Get all files/directories in a directory
    :param directory: path to analyse
    :type directory: str
    :return: list of all files/directories
    :rtype: list
    """
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


EXTRA_FILES = package_files('python_project_starter/template')


setup(
    name='python-project-starter',
    author='Henri Devigne',
    author_email='henri.devigne@bonkgaming.fr',
    url='https://github.com/henri9813/python-project-starter',
    version='1.2',
    description="This package permit you to easily create a new project",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'python-project-starter=python_project_starter.__main__:main'
        ]
    },
    package_data={'': EXTRA_FILES},
    include_package_data=True
)
