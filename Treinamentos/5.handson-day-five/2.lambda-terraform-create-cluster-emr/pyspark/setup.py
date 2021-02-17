from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
    name='pyspark-seed',
    version=__version__,
    packages=find_packages(),
    install_requires=['pyspark', 'boto3']
)

