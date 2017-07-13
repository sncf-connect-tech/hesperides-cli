from setuptools import Command, find_packages, setup

setup(
    # Application name:
    name="hesperides-cli",

    version="0.1.0",

    # Application author details:
    author="Victor SALAUN",
    author_email="victor.salaun@gmail.com",

    # Packages
    packages=find_packages(exclude=['tests*']),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",

    #
    # license="LICENSE.txt",
    description="hesperides-cli",

    entry_points={
        'console_scripts': [
            'hesperides=hesperidescli.Hello:main',
        ],
    },
)
