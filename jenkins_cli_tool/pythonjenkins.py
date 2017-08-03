import jenkins
import pprint

if __name__ == '__main__':
    server = jenkins.Jenkins('http://jenkins-qa.lab.dubl.axway.int:8080', username='chermet', password='Shadow1995!!!')
    print('User: %s' %(server.get_whoami()['fullName']))

    jobs = server.get_all_jobs(3)
    for job in jobs:
        print job['name']

    job_status = server.get_job_info("JenkinsCLITest-Corentin")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(job_status)
    print job_status['url']


