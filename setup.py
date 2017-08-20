from setuptools import find_packages, setup

setup(
    # Application name:
    name="hesperides-cli",

    version="0.2.0",

    # Application author details:
    author="Victor SALAUN",
    author_email="victor.salaun@gmail.com",

    # Packages
    packages=find_packages(exclude=['tests*']),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://pypi.python.org/pypi/hesperides-cli/0.2.0",

    #
    # license="LICENSE.txt",
    description="Command Line Interface for Hesperides https://github.com/voyages-sncf-technologies/hesperides",

    entry_points={
        'console_scripts': [
            'hesperides=hesperidescli.hesperidescli:cli',
        ],
    },

    install_requires=[
        "click"
    ],
)
