from distutils.core import setup

from postbox import __version__

setup(
    name    = 'postbox',
    description = 'Send email easier.',
    long_description = open('README.rst').read(),
    version = __version__,
    author  = 'Mosky',
    author_email = 'mosky.tw@gmail.com',
    #url = 'http://postbox.mosky.tw/',
    url = 'https://github.com/moskytw/postbox',
    py_modules = ['postbox'],
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

