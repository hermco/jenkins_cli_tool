import click

@click.group()
@click.option('debug/no-debug')
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()
def sync():
    click.echo('Synching')

@cli.command()
def blah():
    click.echo('blah')

if __name__ == '__main__':
    cli()
