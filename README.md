# HESPERIDES CLI

[![Build Status](https://travis-ci.org/victorsalaun/hesperides-cli.svg?branch=master)](https://travis-ci.org/victorsalaun/hesperides-cli)

Command Line Interface for Hesperides https://github.com/voyages-sncf-technologies/hesperides

## Prerequisites

- python 3 >= 3.4

## Installation

hesperides-cli has been registered. It can be installed via pip:

    pip install hesperides-cli

## Build

    python3 setup.py install

For development purpose:

    python3 setup.py develop

## Usage

    hesperides [OPTIONS] COMMAND [ARGS]

### Configure

To set up your environment:

    hesperides set-conf
    hesperides set-profile [PROFILE_NAME]