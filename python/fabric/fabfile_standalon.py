# -*- coding: utf-8 -*-
"""
fabfile template to deploy project to server

- Requirements:
    fabric==2.5.0

- Usage:
    fab -H my-server deploy

"""

import traceback
import logging
from invoke import task

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

WORK_DIR = '/deploy'

# file storage last git commit id
LAST_CID_FILE = "last_commit_id.txt"


@task
def deploy(c):
    logger.info("Deploying on {}".format(c.host))
    with c.cd(WORK_DIR):
        # Create last commit id file if not exists
        if c.run('test -f {}'.format(LAST_CID_FILE), warn=True).failed:
            logger.info("Create {} file".format(LAST_CID_FILE))
            save_last_commit(c)

        do_deploy(c)

        notify_commit_applied(c)
        save_last_commit(c)


def do_deploy(c):
    c.run('git pull')
    # c.run('docker-compose build demo')
    # c.run('docker-compose up -d demo')

# Utils functions
# -----------------------------------------
def run(c, command, capture=False):
    result = c.run(command, echo=True)
    if capture:
        return result.stdout.strip()
    return result


def get_current_commit(c):
    return run(c, "git rev-parse HEAD", True)


def save_last_commit(c):
    run(c, "git rev-parse HEAD > {}".format(LAST_CID_FILE))


def get_last_commit(c):
    return run(c, "cat {}".format(LAST_CID_FILE), True)


def get_git_logs(c, last_commit_id, current_commit_id):
    return run(c, "git log {}...{} --oneline --pretty=format:'%s'".format(last_commit_id, current_commit_id), True)


def notify_commit_applied(c):
    last_commit_id = get_last_commit(c)
    current_commit_id = get_current_commit(c)
    commit_applied = get_git_logs(c, last_commit_id, current_commit_id)
    if commit_applied:
        commit_applied = "••• " + commit_applied
        commit_applied = commit_applied.replace("\n", "\n••• ")
    else:
        commit_applied = 'No commit applied!'
    attachments = [
        {
            "color": "good",
            "title": "Commit applied:",
            "text": commit_applied,
        },
    ]
    logger.info(commit_applied)
    # sc.send(attachments=attachments, text="Deploy to *{}* success".format(c.host))
