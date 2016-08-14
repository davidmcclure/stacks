

from setuptools import setup, find_packages


setup(

    name='stacks',
    version='0.1.0',
    description='A corpus manager for the Stanford Literary Lab',
    url='https://github.com/davidmcclure/stacks',
    license='MIT',
    author='David McClure',
    author_email='dclure@stanford.edu',
    packages=find_packages(),
    scripts=['bin/stacks'],

)
