# HESPERIDES CLI

[![TravisCI build Status](https://travis-ci.org/voyages-sncf-technologies/hesperides-cli.svg?branch=master)](https://travis-ci.org/voyages-sncf-technologies/hesperides-cli) [![Coverage Status](https://coveralls.io/repos/github/voyages-sncf-technologies/hesperides-cli/badge.svg?branch=master)](https://coveralls.io/github/voyages-sncf-technologies/hesperides-cli?branch=master) [![Pypi latest version](https://img.shields.io/pypi/v/hesperides-cli.svg)](https://pypi.python.org/pypi/hesperides-cli) [![Supported Python versions](https://img.shields.io/pypi/pyversions/hesperides-cli.svg)](https://pypi.python.org/pypi/hesperides-cli) [![License](https://img.shields.io/pypi/l/hesperides-cli.svg)](https://pypi.python.org/pypi/hesperides-cli)

Python Command Line Interface for Hesperides https://github.com/voyages-sncf-technologies/hesperides


## Installation

`hesperides-cli` is published on [Pypi](https://pypi.python.org/pypi/hesperides-cli). It can be installed simply with `pip`:

    pip install hesperides-cli

### Developper environment installation
After cloning this repo and optionally creating a [virtualenv](https://github.com/berdario/pew):

    pip install -e .


## Usage

    hesperides [OPTIONS] COMMAND [ARGS]

To get all hesperides commands, just type:

    hesperides

### Configure

This client configuration is stored locally in `~/.hesperides/`:

To set up your environment and create a local user profile by answering to a few questions:

    hesperides set-conf [PROFILE_NAME]
    
If you have multiple profiles, you can switch between them with:

    hesperides use-profile [PROFILE_NAME]

To try your configuration, type one of these commands:

    hesperides get-versions
    hesperides get-user
    hesperides get-stats
