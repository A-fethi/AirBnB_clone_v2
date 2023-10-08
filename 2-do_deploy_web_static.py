#!/usr/bin/python3
from fabric.api import *
import os.path


env.hosts = ['52.205.80.117', '54.236.17.184']


def do_deploy(archive_path):
    """A script that distributes an archive to web servers"""
    try:
        if not os.path.exists(archive_path):
            return False
        file_path = os.path.basename(archive_path)
        name = os.path.splitext(file_path)[0]
        put(archive_path, "/tmp/")
        run("rm -rf /data/web_static/releases/{}".format(name))
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(file_path, name))
        run("rm /tmp/{}".format(file_path))
        run("mv /data/web_static/releases/{0}/web_static/* \
            /data/web_static/releases/{0}/".format(name))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed!")
        return True
    except Exception:
        return False
