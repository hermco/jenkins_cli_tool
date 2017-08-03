from distutils.core import setup
from setuptools import *


setup(
    name='jenkins_cli_tool',
    version='2.1.0',
    packages=find_packages(),
    url='https://github.com/hermco/jenkins_cli_tool',
    license='MIT',
    author='chermet',
    author_email='chermet@axway.com',
    description='None',
    install_requires=[
       'click',
       'python-jenkins'
    ],
    entry_points={
        'console_scripts': [
            'jenkins-cli-tool = jenkins_cli_tool.startjob:main'
        ]
    }
)