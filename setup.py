from setuptools import setup, find_packages

setup(
    # Metadata
    name='my_test_pkg',
    version='0.5.0',
    author='Filip Kovacevic',
    author_email='f.kovacevic@gmx.at',
    license='GNU General Public License (GPL)',
    description="A test package",
    long_description="A test package long",
    url='https://github.com/GreenfishK/test_repository',

    # Package data
    packages=find_packages(include=['my_test_pkg']),
    # package_data={'my_test_package', ['*.db', '*.sql*, '*.txt.*'],
    # include_package_data=True,

    # Build and install Requirements
    install_requires=[
        'python>=3.8',
        'matplotlib>=3.3.2',
        'numpy >=1.18', 
        'pandas >=1.1.2' 
    ],
    # extras_require={ 'interactive': ['matplotlib>=2.2.0,, 'jupyter'],
    build=['python', 'conda', 'conda-build', 'anaconda-client', 'setuptools']  # 'twine', 'wheel'

    # Entry points
    # entry_points={'console_scripts': ['my-command=exampleproject.example:main']}
    
    # Tests
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],

    # Flake8
    # setup_requires=['flake8']

)
