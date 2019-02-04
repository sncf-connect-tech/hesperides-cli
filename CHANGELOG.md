# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [v0.3.0] - Work In Progress
### Changed
- Renamed `applications import get_application_from_module` as `get_applications_using_module`
- Shortened import paths: no more `$resource.$resource`

### Added
- `black` code formatter
- New commands to generate & validate local files based on templates:

    hesperides local-generate-files tests/descriptor.json
    hesperides local-validate-files tests/descriptor.json


## [v0.2.0] - 2017-08-31
## Added
- `modules` commands

### Fixed
- Several bugs


## [v0.1.0] - 2017-08-18
Initial version
