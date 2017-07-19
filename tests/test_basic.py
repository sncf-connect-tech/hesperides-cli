import click


def test_basic_functionality(runner):
    @click.command()
    def cli():
        """Hello World!"""
        click.echo('I EXECUTED')

        result = runner.invoke(cli, ['--help'])
        assert not result.exception
        assert result.exit_code == 0
