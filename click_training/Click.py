import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
@click.argument('lol')
def hello(count, name, lol):
    count=3
    for x in range(count):
        click.echo('Hello %s %s!' %(name , lol) )

if __name__ == '__main__':
    hello()

