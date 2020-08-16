# Reference :  Setup script documentation 
# https://setuptools.readthedocs.io/en/latest/setuptools.html

from setuptools import setup, find_packages

def get_requirements(filename):
    with open(filename) as f:
        requirements = f.read().splitlines()
    return requirements

setup(name='sample package',
      version='1.0',
      description='CSC 510: Software Engineering Project 1',
      author='Omkar Kulkarni',
      author_email='omkar.omkar.135@gmail.com',
      license="MIT",
      url='https://github.com/txt/se20/blob/master/docs/h01work.md',
      packages=find_packages(),
      python_requires=">=3.6",
      install_requires = get_requirements("requirements.txt"),
      include_package_data=True,
     )