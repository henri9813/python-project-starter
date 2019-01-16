from setuptools import setup, find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('python_project_starter/template')


setup(
    name='python-project-starter',
    author='Henri Devigne',
    author_email='henri.devigne@bonkgaming.fr',
    url='https://github.com/henri9813/python-project-starter',
    version='1.0',
    description="This package permit you to easily create a new project",
    long_description=long_description,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'python-project-starter=python_project_starter.__main__:main'
        ]
    },
    package_data={'': extra_files},
    include_package_data=True
)
