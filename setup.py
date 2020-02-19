from setuptools import setup
from plancklensing import __author__, __version__
import os

file_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(file_dir)

setup(name="plancklensing",
      version=__version__,
      author=__author__,
      license='LGPL',
      description='Example external Cobaya likelihood package: Planck 2018 lensing',
      zip_safe=False,  # set to false if you want to easily access bundled package data files
      packages=['plancklensing', 'plancklensing.tests'],
      package_data={'plancklensing': ['*.yaml', '*.bibtex', 'data_2018/*', 'data_2018/**/*']},
      install_requires=['cobaya>=2.0.5'],
      test_suite='plancklensing.tests',
      tests_require=['camb>=1.0.5']
      )
