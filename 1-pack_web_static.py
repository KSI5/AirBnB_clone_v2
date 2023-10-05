#!/usr/bin/env python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the web_static folder."""
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None
