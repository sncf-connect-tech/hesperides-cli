# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [v0.3.0] - Work In Progress
### Changed
- Renamed `delete-module-workingcopy-template` into `create-module-workingcopy-template` (it was terribly badly named)
- Renamed `get_application_from_module` into `get_applications_using_module`
- Renamed `set-profile` into `use-profile`
- Renamed `--long_options` into `--long-options`
- Transformed some `--options` into positionnal arguments in `get-application`, `perform-search-applications`,
`create-application-platform`, `update-application-platform`, `delete-profile`, `set-conf`, `create-module` & `create-module-workingcopy-template`
- Replaced `set-config` option `--response-format` by `--ignore-ssl-warnings`
- Shortened import paths: no more `$resource.$resource`

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


## [v0.2.0] - 2017-08-31
## Added
- `modules` commands

### Fixed
- Several bugs


## [v0.1.0] - 2017-08-18
Initial version
