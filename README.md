# HESPERIDES CLI

[![TravisCI build Status](https://travis-ci.org/voyages-sncf-technologies/hesperides-cli.svg?branch=master)](https://travis-ci.org/voyages-sncf-technologies/hesperides-cli) [![Coverage Status](https://coveralls.io/repos/github/voyages-sncf-technologies/hesperides-cli/badge.svg?branch=master)](https://coveralls.io/github/voyages-sncf-technologies/hesperides-cli?branch=master) [![Pypi latest version](https://img.shields.io/pypi/v/hesperides-cli.svg)](https://pypi.python.org/pypi/hesperides-cli) [![Supported Python versions](https://img.shields.io/pypi/pyversions/hesperides-cli.svg)](https://pypi.python.org/pypi/hesperides-cli) [![License](https://img.shields.io/pypi/l/hesperides-cli.svg)](https://pypi.python.org/pypi/hesperides-cli)

Python 3 lib & CLI (_Command Line Interface_) for [Hesperides](https://github.com/voyages-sncf-technologies/hesperides)

A changelog is available here: [CHANGELOG.md](CHANGELOG.md)


## Installation

`hesperides-cli` is published on [Pypi](https://pypi.python.org/pypi/hesperides-cli). It can be installed simply with `pip`:

    pip install hesperides-cli

### Developper environment installation
After cloning this repo and optionally creating a [virtualenv](https://github.com/berdario/pew):

    pip install -e .

### Releasing a new version
With a valid `~/.pypirc`:

1. update `CHANGELOG.md`
2. bump version in `hesperidescli/hesperidescli.py`
3. `python setup.py sdist`
4. `twine upload dist/*`
5. `git tag $version && git push && git push --tags`


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

### Usage with Docker

You can using the following `Dockerfile` as a starting point:

    FROM python:3
    RUN pip install hesperides-cli
    ARG USERNAME
    ARG PASSWORD
    RUN hesperides set-conf --username $USERNAME --password $PASSWORD --hesperides-endpoint https://hesperides.example --ignore-ssl-warnings
    ENTRYPOINT ["hesperides"]

The resulting Docker image will contain some secret credentials, which is **not** a good practice,
but makes it really easy to use for demos:

    docker build --build-arg USERNAME=... --build-arg PASSWORD=... -t hesperides-cli .
    docker run --rm hesperides-cli get-versions

If your goal is instead to generate files in your Docker image at startup time,
you can start by putting something like this in your _entrypoint_:

    hesperides write-files --app $APP --ptf $PTF

### Local files generation with zero calls to the backend API

_cf._ [hesperidescli.local](hesperidescli/local)
