#!/usr/bin/python3
"""Script that generates a .tgz archive from the contents of the web_static
"""

import tarfile
from fabric.api import *
from datetime import datetime


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

    if status == 0:
        return "versions/{}".format(file_name)
    else:
        return None
