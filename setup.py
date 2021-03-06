from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "A simple lightweight python wrapper for the Azure Bing Search API."
VERSION = '0.2.6'
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    'Topic :: Software Development :: Libraries :: Python Modules',
]

KEYWORDS = ['Azure', 'Bing', 'API', 'Search']

INSTALL_REQUIRES = [
    'requests',
]

setup(
    name='py-bing-search',
    #packages = ['py_bing_search'],
    packages = find_packages(),
    version=VERSION,
    author=u'Tristan Tao',
    author_email='tristan@teamleada.com',
    url='https://github.com/tristantao/py-bing-search',
    license='MIT',
    keywords=KEYWORDS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    test_suite='nose.collector',
    tests_require=['nose'],
)
