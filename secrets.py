import json
from os import environ, path

def get_secrets_for(identifier):
    # get wordnik and twitter keys from ${OPENSHIFT_DATA_DIR}secrets.json
    datadir = environ['OPENSHIFT_DATA_DIR']
    secrets_file = path.join(datadir, '{}.json'.format(identifier))
    with open(secrets_file) as secrets_data:
        secrets = json.load(secrets_data)
    return secrets
