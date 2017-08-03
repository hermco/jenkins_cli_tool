import jenkins
import pprint
import click


@click.group()
@click.option('--job_name', help='Jenkins job name.', prompt=True)
def start():
    global server
    server = jenkins.Jenkins('http://jenkins-qa.lab.dubl.axway.int:8080', username='chermet', password='Shadow1995!!!')

@start.command()
@click.option('--job_name', help='Jenkins job name.', prompt=True)
def startJob(job_name):
    server.build_job(job_name,parameters=None,token="62ebe5c65b3231d233ea1eaa106a642f")

#@click.option('--job_name', help='Jenkins job name.', prompt=True)
@start.command()
def jobExists(job_name):
    return server.job_exists(job_name)

@click.group()
@click.option('--job_nameaa', help='Jenkinzeazeaze.', prompt=True)
def start2():
    pass

@start2.command()
@click.option('--job_nameaa', help='Jenkinzeazeaze.', prompt=True)
def aa():
    pass

cli = click.CommandCollection(sources=[start, start2])

if __name__ == '__main__':
    cli()

