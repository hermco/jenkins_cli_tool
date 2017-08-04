import click
from startjob import command as startjob
from startAndMonitor import command as startAndMonitor


class Jenkins(object):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password


@click.group()
@click.option('--url',help='Protocol+Url+Port of the Jenkins server. [required]')
@click.option('--username',help='Username. [required]')
@click.option('--password',help='Password. [required]')
@click.pass_context
def entry_point(ctx,url,username, password):
    ctx.obj = Jenkins(url,username,password)

entry_point.add_command(startjob.startjob)
entry_point.add_command(startAndMonitor.startAndMonitor)


if __name__ == '__main__':
    entry_point()

