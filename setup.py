"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject

this was taken and modified from https://aur.archlinux.org/cgit/aur.git/?h=kindleunpack
Commit https://aur.archlinux.org/cgit/aur.git/commit/?h=kindleunpack&id=a6a60981682c40504c921ef8e9703e25adb65579
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os, shutil

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Fix linux not importing pyw modules.
shutil.copyfile('KindleUnpack.pyw', 'KindleUnpack.py')

# Create root __init__
# open('__init__.py', 'a').close()  # not eneeded for https://github.com/clach04/KindleUnpack

setup(
    name='KindleUnpack',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.83',

    description='Extract text, images and metadata from Kindle/Mobi files',

    # The project's main homepage.
    url='http://www.mobileread.com/forums/showthread.php?t=61986',
    download_url='https://github.com/kevinhendricks/KindleUnpack/releases',

    # Author details
    author='Charles M. Hannum',
    author_email='root@ihack.net',
    maintainer='Kevin Hendricks',
    maintainer_email='kevinhendricks@users.noreply.github.com',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GPLv3 License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='mobi kf8 ebooks',

    # Remap package root structure
    package_dir={'KindleUnpack' : ''},

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['KindleUnpack', 'KindleUnpack.lib', 'KindleUnpack.libgui'],

    zip_safe=False,
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'kindleunpack-cli=KindleUnpack.lib.kindleunpack:main',
        ],
        'gui_scripts': [
            'kindleunpack-gui=KindleUnpack.KindleUnpack:main',
        ],
    },
)
