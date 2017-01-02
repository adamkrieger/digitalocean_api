#!/usr/bin/env python
"""http://jessenoller.com/blog/2009/02/05/ssh-programming-with-paramiko-completely-different"""

import argparse
import paramiko

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--ip', help='IP of the destination machine.')

#Main Line
ARGUMENTS = PARSER.parse_args()

SSH = paramiko.SSHClient()

SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

SSH.connect(ARGUMENTS.ip, username='root')

STDIN, STDOUT, STDERR = SSH.exec_command("uptime")

print STDOUT.readlines()

SSH.close()
