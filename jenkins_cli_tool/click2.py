import jenkins
import pprint
import click

@click.group()
def cli():
    global server
    server = jenkins.Jenkins('http://jenkins-qa.lab.dubl.axway.int:8080', username='chermet', password='Shadow1995!!!')

@cli.command()
def sync():
    print('Synching')

if __name__ == '__main__':
    cli()