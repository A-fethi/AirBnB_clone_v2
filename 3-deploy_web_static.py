#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
import os.path


env.hosts = ["54.160.99.253", "100.25.14.73"]


@runs_once
def do_pack():
    """A script that generates a .tgz archive from the contents
    of the web_static folder"""
    now = datetime.now()
    time_str = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(time_str)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_name))
        return (archive_name)
    except Exception:
        return None


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


def deploy():
    """Creates and distribute an archive to a web server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
