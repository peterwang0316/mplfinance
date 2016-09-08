from setuptools import setup

setup(name='mpl_finance',
      version='0.10.0',
      author='MPL Developers',
      author_email='matplotlib-users@python.org',
      py_modules=['mpl_finance'],
      description='Finance plots using matplotlib',
      url='http://github.com/matplotlib/finance',
      platforms='Cross platform (Linux, Mac OSX, Windows)',
      install_requires=['matplotlib'],
      license="BSD",
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   ],
      keywords='finance',
      )
