Those commands let you generate local files based on versioned Hesperides template
and custom development values stored in a JSON descriptor file:

    hesperides local-generate-files tests/descriptor.json
    hesperides local-validate-files tests/descriptor.json

Those commands make **zero HTTP call** to the Hesperides API.

The JSON descriptors manipulated by those 2 commands match the format of the ones used by [hesperides-jenkins-lib](https://github.com/voyages-sncf-technologies/hesperides-jenkins-lib/blob/master/vars/hesperides.txt#L163).

In addition, it support an extra `local` entry at the template-file definition level, that contains :
- an optional `values` mapping containing values for the template mustaches
- optional key / values overrides to be applied at the template-file level above: `title`, `filename`, `location`

For an example, check [tests/descriptor.json](https://github.com/Lucas-C/hesperides-cli/blob/master/tests/descriptor.json).
