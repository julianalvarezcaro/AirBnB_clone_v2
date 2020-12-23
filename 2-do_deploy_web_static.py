#!/usr/bin/python3
"""Script that distributes an archive to your web servers
"""

from fabric.api import *
from os.path import exists

env.hosts = ['35.196.70.139', '34.75.17.16']


def do_deploy(archive_path):
    """Distributes an archive to your web servers
    """

    if not exists(archive_path):
        return False

    try:
        file_nametgz = archive_path.split("/")[-1]
        file_name = file_nametgz.split(".")[0]
        print("Before")
        put(archive_path, "/tmp/{}".format(file_nametgz))
        print("After")
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("tar -xzf /tmp/{} -C\
            /data/web_static/releases/{}/".format(file_nametgz, file_name))

        run("rm /tmp/{}".format(file_nametgz))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))

        # Deletes the symbolic link?
        run("rm -rf /data/web_static/current")

        # Creates the symbolic link again
        run("ln -s /data/web_static/releases/{}/\
            /data/web_static/current".format(file_name))
        return True
    except Exception as e:
        print(e)
        return False
