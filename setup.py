from setuptools import setup
from plancklens import __author__, __version__

setup(name="plancklens",
      version=__version__,
      author=__author__,
      license='LGPL',
      description='Example external Cobaya likelihood package: Planck 2018 lensing',
      zip_safe=False,  # set to false if you want to easily access bundled package data files
      packages=['plancklens', 'plancklens.tests'],
      package_data={'plancklens': ['data_2018/*', 'data_2018/**/*']},
      install_requires=['cobaya>=2.0.4'],
      test_suite='plancklens.tests',
      tests_require=['camb>=1.0.5']
      )
