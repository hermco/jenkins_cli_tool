from distutils.command import build
import jenkins
import pprint
import click
from time import sleep
import sys
import getopt
import ast

pp = pprint.PrettyPrinter(indent=4)


def startJob(jobName, login, pwd, server, port,parameters, wait):
    server = jenkins.Jenkins('http://' + server + ':' + port, username=login, password=pwd)
    try:
        next_build_number = server.get_job_info(jobName)['nextBuildNumber']
    except jenkins.NotFoundException:
        print "NotFoundException when looking for job with name '%s'." % jobName
        exit(1)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    print "Starting %s , build #%s." % (jobName, next_build_number)
    try:
        server.build_job("JenkinsCLITest-Corentin", parameters, token=None)
    except:
        pp.pprint(sys.exc_info())
        print "Please verify your parameters (especially choice parameters - are the values chosen authorized?"
        exit(2)

    stop = False
    while not stop:
        try:
            build_info = server.get_build_info(jobName, next_build_number)
        except jenkins.NotFoundException:
            print "NotFoundException when looking for build #%s : build probably still in the queue. Waiting %d sc until next retry." % (next_build_number, wait)
            sleep(wait)
            pass
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        else:
            if build_info['result'] == 'SUCCESS':
                print "Build #%s finished with result : SUCCESS." % next_build_number
                exit(0)
            elif build_info['result'] == 'FAILED':
                print "Build #%s finished with result : FAILED." % next_build_number
                stop = True
                exit(3)
            elif build_info['result'] == None and build_info['building'] == True:
                print "Build #%s is not finished yet. Waiting %d sc until next check." % (next_build_number,wait)
                sleep(wait)
            else:
                print "Unknown build result. Full trace below:"
                pp.pprint(build_info)


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "",
                                   ["login=","pwd=","server=","port=","jobName=","parameters=","wait=","default","help"])
    except getopt.GetoptError:
        print "Incorrect arguments."
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("--login"):
            login = arg
        elif opt in ("--pwd"):
            pwd = arg
        elif opt in ("--server"):
            server = arg
        elif opt in ("--port"):
            port = arg
        elif opt in ("--jobName"):
            jobName = arg
        elif opt in ("--parameters"):
            parameters = ast.literal_eval(arg)
        elif opt in ("--wait"):
            wait = int(arg)
        elif opt in ("--help"):
            print ("Usage: python startJob \n"
                   "--login <login>\n"
                   "--pwd <pwd>\n"
                   "--server <server>\n"
                   "--port <port>\n"
                   "--jobName <jobName>\n"
                   "--parameters \"{'XXXX':'YYYY', ...}\"\n"
                   "--wait <time to wait between each retry to check for build status>\n"
                   "--help\n"
                   "--default")
            exit(0)
        elif opt in ("--default"):
            login = "chermet"
            pwd = "Shadow1995!!!"
            server = "jenkins-qa.lab.dubl.axway.int"
            port = "8080"
            jobName = "JenkinsCLITest-Corentin"
            parameters = {'THREADS': 'AAAA', 'IDK': 'value2'}
            wait = 5
    startJob(jobName, login, pwd, server, port, parameters,wait)


#--login chermet --pwd Shadow1995!!! --server jenkins-qa.lab.dubl.axway.int --port 8080 --jobName JenkinsCLITest-Corentin --parameters "{'THREADS': 'AAAA', 'IDK': 'value2'}"
#--login chermet --pwd Shadow1995!!! --default