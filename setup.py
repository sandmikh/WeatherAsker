from setuptools import setup, find_packages

from weatherChecker import main


setup(
	name='HI travel',
    version='1.0',
    packages=find_packages(),
    long_description=open('README.txt').read(),

    entry_points={
        'console_scripts':
            ['wc = weatherChecker.main:start']
        }
)