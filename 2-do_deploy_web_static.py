#!/usr/bin/env python3
from fabric.api import env, put, run, local
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract archive to /data/web_static/releases/
        archive_filename = archive_path.split("/")[-1]
        archive_no_extension = archive_filename.split(".")[0]
        remote_path = "/data/web_static/releases/"

        run("mkdir -p {}{}".format(remote_path, archive_no_extension))
        run("tar -xzf /tmp/{} -C {}{}/".format(archive_filename, remote_path, archive_no_extension))
        run("rm /tmp/{}".format(archive_filename))

        # Delete and recreate symbolic link
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(remote_path, archive_no_extension))

        return True
    except Exception:
        return False
