jenkins_cli_tool
================

Jenkins CLI Tool

Usage
-----

`jenkins-cli-tool --help`
`jenkins-cli-tool <command> --help`

Exemple:
`jenkins-cli-tool --url http://jenkins-qa.lab.dubl.axway.int:8080 --username <USERNAME> --password <YOURPASSWD> startandmonitor --job JenkinsCLITest-Corentin --parameters "{'THREADS': 'AAAA', 'IDK': 'value2'}" --wait 5`
(change username and password)

Installation
------------

`pip install jenkins-cli-tool`

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`jenkins_cli_tool` was written by `Corentin Hermet <chermet@axway.com>`_.
