#!/usr/bin/env python
"""droplet_run.py - Connects to the given IP by SSH, then runs a container
    with the given image.
    - Assumes you have SSH private key to the destination in user folder.
    - Assumes that the image is on docker hub rather than on a custom registry.
    - Always detaches.
"""

import paramiko
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--ip', help='IP of the destination machine.')
PARSER.add_argument('--image', help='Name of the docker image.')
PARSER.add_argument('--name', help='Name for the container.')
PARSER.add_argument('--args', default='', help='Additional docker run arguments.')

def build_docker_command(image, name, args):
    """Builds docker run command."""
    return 'docker run -d --name {0} {1} {2}'.format(
        name, args, image
    )

#Main Line
ARGUMENTS = PARSER.parse_args()

SSH = paramiko.SSHClient()

SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

SSH.connect(ARGUMENTS.ip, username='root')

DOCKER_RUN_COMMAND = build_docker_command(
    ARGUMENTS.image,
    ARGUMENTS.name,
    ARGUMENTS.args
)

print DOCKER_RUN_COMMAND

STDIN, STDOUT, STDERR = SSH.exec_command(DOCKER_RUN_COMMAND)

STDIN.close()

for line in iter(lambda: STDOUT.readline(2048), ""):
    print line

SSH.close()
