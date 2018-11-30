import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pldp',
    version='0.1',
    packages=['pldp'],
    include_package_data=True,
    license='MIT License',
    description='PLDP models for Django',
    long_description=README,
    url='https://datamade.us/',
    author='DataMade, LLC',
    author_email='info@datamade.us',
    install_requires=[
        'Django<2.2',
        'django-languages-plus==1.0.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
