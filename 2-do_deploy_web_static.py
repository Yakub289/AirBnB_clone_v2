#!/usr/bin/python3

"""Compress web static package"""

from fabric.api import *
from datetime import datetime
from os import path


env.hosts ['100.25.181.32', '54.237.98.247']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web files to server"""
    if not os.path.exists(archive_path):
        return False
    try:
        pname = archive_path.replace('/', ' ')
        pname = shlex.split(pname)
        pname = pname[-1]

        wname = pname.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(pname)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except BaseException:
        return False
