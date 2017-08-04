import click
import sys
import ast
import pprint
import jenkins as jenkinsapi
from time import sleep


@click.command()
@click.option('--job',required=True,help='Name of the job to start.')
@click.option('--parameters',required=False, help='Job\s parameters.')
@click.pass_obj
def startjob(jenkins,job, parameters):
    """Starts a Jenkins job."""
    pp = pprint.PrettyPrinter(indent=4)
    server = jenkinsapi.Jenkins(jenkins.url, username=jenkins.username, password=jenkins.password)
    try:
        next_build_number = server.get_job_info(job)['nextBuildNumber']
    except jenkinsapi.NotFoundException:
        print "NotFoundException when looking for job with name '%s'." % job
        exit(1)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    print "Build #%s of %s started." % (next_build_number,job)
    try:
        server.build_job("JenkinsCLITest-Corentin", ast.literal_eval(parameters), token=None)
    except:
        pp.pprint(sys.exc_info())
        print "Please verify your parameters (especially choice parameters - are the values chosen authorized?"
        exit(2)