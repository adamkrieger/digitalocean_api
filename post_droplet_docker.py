#!/usr/bin/env python
"""Creates a droplet with the docker default img
    Ex: python post_droplet_docker.py --name droplettest --ssh_path ~/.ssh/keyfingerprint
    Contents of fingerprint file example:
    de:aa:bb:cc:5c:5a:39:1e:11:22:33:44:55:66:cb:c4
    Example of command to gen (also a little manual work to get just the hex seq):
    ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub > ~/.ssh/keyfingerprint
    """

#curl -X POST -H "Content-Type: application/json"
#   -H "Authorization: Bearer $DO_TOKEN" \
#	-d '{"name":"example.com","region":"tor1","size":"512mb",
#   "image":"docker-16-04","ssh_keys":null,"backups":false,
#   "ipv6":true,"user_data":null,"private_networking":null,
#   "volumes": null,"tags":["web"]}' "https://api.digitalocean.com/v2/droplets"

import httplib
import os
import json
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--name', help='Name of the impending droplet.')
PARSER.add_argument('--ssh_path', help='Fingerprint of DigitalOcean-stored SSH key.')

def create_droplet(name, ssh_key):
    """Contacts DO to create the droplet"""

    ssh_keys = []
    if ssh_key:
        ssh_keys.append(ssh_key)

    create_args = dict()
    create_args['name'] = name
    create_args['region'] = 'tor1'
    create_args['size'] = '512mb'
    create_args['image'] = 'docker-16-04'
    create_args['ssh_keys'] = ssh_keys

    token = os.environ['DO_TOKEN']

    url_root = "api.digitalocean.com"
    url_suffix = "/v2/droplets"
    header = {
        "Content-type": "application/json",
        "Authorization": "Bearer {0}".format(token)
        }
    body = json.dumps(create_args)
    connection = httplib.HTTPSConnection(url_root)

    connection.request('POST', url_suffix, body, header)
    response = connection.getresponse()
    content = response.read()

    return content

ARGUMENTS = PARSER.parse_args()

print "Attempting to create droplet."

SSH_FILE = open(ARGUMENTS.ssh_path, 'r')
SSH_FILE_CONTENTS = SSH_FILE.readlines()
SSH_FINGERPRINT = ''.join(SSH_FILE_CONTENTS).strip()

RESULT = create_droplet(ARGUMENTS.name, SSH_FINGERPRINT)

print RESULT
