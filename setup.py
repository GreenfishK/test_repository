from setuptools import setup

setup(
   name='my_test_pkg',
   version='1.0',
   description='A useful module',
   author='Filip Kovacvic',
   author_email='f.kovacevic@gmx.at',
   packages=['my_test_pkg'],  #same as name
   # install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)
