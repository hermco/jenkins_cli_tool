from distutils.core import setup

setup(
    name='jenkins_cli_tool',
    version='3.1',
    packages=['cli', 'cli.startjob', 'cli.startAndMonitor', 'tests'],
    url='https://github.com/hermco/jenkins_cli_tool',
    license='MIT',
    author='chermet',
    author_email='chermet@axway.com',
    description='CLI tool for Jenkins',
    install_requires=[
       'click',
       'python-jenkins'
    ],
    entry_points={
        'console_scripts': [
            'jenkins-cli-tool = cli.cli:entry_point'
        ]
    }
)
