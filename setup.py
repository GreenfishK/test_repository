from setuptools import setup, find_packages

setup(
    # Metadata
    name="my_test_pkg",
    version="0.7.0",
    author="Filip Kovacevic",
    author_email="f.kovacevic@gmx.at",
    description="A test description",
    license="GPL",
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    long_description="A long description",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],

    # Packaging
    packages=find_packages(
        where='src',
        include=['my_test_pkg'],
    ),
    package_dir={"": "src"}
)