# HESPERIDES CLI

[![Build Status](https://travis-ci.org/victorsalaun/hesperides-cli.svg?branch=master)](https://travis-ci.org/victorsalaun/hesperides-cli)

Command Line Interface for Hesperides https://github.com/voyages-sncf-technologies/hesperides

## Prerequisites

- python 3 >= 3.4

## Installation

hesperides-cli has been registered. It can be installed via pip:

    pip install hesperides-cli

## Build

    python setup.py install

For development purpose:

    python setup.py develop

## Usage

    hesperides [OPTIONS] COMMAND [ARGS]

To get all hesperides commands, just type:

    hesperides

### Configure

To set up your environment:

    hesperides set-conf
    
Once your configuration is set, you can start using it with:

    hesperides set-profile [PROFILE_NAME]

To try your configuration, type one of these commands:

    hesperides get-versions
    hesperides get-user
    hesperides get-stats
    