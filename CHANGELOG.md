# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [v0.4.1] - 2019-12-12
### Fixed
- `write-files` when module selection options are provided

### Changed
- `get-files` & `write-files` now accept a `--working-copy/--release` switch argument
- `write-files` now allow any number of selectors: `--path` / `--module-name` / `--module-version` / `--working-copy` / `--release` / `--instance-name`

## [v0.4.0] - 2019-12-05
### Fixed
- `get-files` command, which was very buggy
- `perform-search-application-platforms` command, whose query params were incorrect

### Added
- `write-files` command.
Usage example: `hesperides write-files --app KTN --ptf TEST --path '#VSL#WAS' --module-name demoKatana-war --module-version 1.0.0.1 --working-copy`
- `--verbose` optional global parameter
- displaying warnings in case HTTP calls are made to deprecated endpoints


## [v0.3.3] - 2019-11-06
### Changed
- the error message when no profile is configured is more explicit

### Added
- `--version` argument


## [v0.3.2] - 2019-06-26
### Changed
- Renamed `delete-module-workingcopy-template` into `create-module-workingcopy-template` (it was terribly badly named)
- Renamed `get_application_from_module` into `get_applications_using_module`
- Renamed `set-profile` into `use-profile`
- Renamed `--long_options` into `--long-options`
- Transformed some `--options` into positionnal arguments in `get-application`, `perform-search-applications`,
`create-application-platform`, `update-application-platform`, `delete-profile`, `set-conf`, `create-module` & `create-module-workingcopy-template`
- Replaced `set-config` option `--response-format` by `--ignore-ssl-warnings`
- Shortened import paths: no more `$resource.$resource`
- Switching from deprecated endpoints to new ones: `/technos` & using `GET` for searches

### Added
- `applications.get_applications`
- New commands to generate & validate local files based on templates:

    hesperides local-generate-files tests/descriptor.json
    hesperides local-validate-files tests/descriptor.json

- `black` code formatter

### Fixed
- `module_version` parameter was ignored in `create_module_release`

### Deprecated
- All the `cache`, `feedback`, `indexation`, `snapshots` & `stats` commands


## [v0.3.1] - 2018-03-12


## [v0.2.0] - 2017-08-31
## Added
- `modules` commands

### Fixed
- Several bugs


## [v0.1.0] - 2017-08-18
Initial version
