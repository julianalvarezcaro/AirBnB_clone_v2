#!/usr/bin/python3
"""Creates and distributes an archive to your web servers
"""
from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['35.196.70.139', '34.75.17.16']


def do_pack():
    """Folder: web_static
    Stored in folder: versions
    Archive's name: web_static_<year><month><day><hour><minute><second>.tgz
    Return:
        Success: archive path
        Otherwise: None
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_" + time + ".tgz"
    local("mkdir -p versions")
    status = local("tar -czvf versions/{} web_static/".format(file_name))

    if status.succeeded:
        print("Exit with 0")
        return "versions/{}".format(file_name)
    else:
        print("Returning None")
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers
    """

    if not exists(archive_path):
        return False

    try:
        file_nametgz = archive_path.split("/")[-1]
        file_name = file_nametgz.split(".")[0]
        print("Bef: {}".format(archive_path))
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
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
