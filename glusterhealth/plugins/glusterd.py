#
# Copyright (c) 2017 Red Hat, Inc.
#
# This file is part of libgfapi-python project which is a
# subproject of GlusterFS ( www.gluster.org)
#
# This file is licensed to you under your choice of the GNU Lesser
# General Public License, version 3 or any later version (LGPLv3 or
# later), or the GNU General Public License, version 2 (GPLv2), in all
# cases as published by the Free Software Foundation.

import logging

from utils import command_output, CommandError


def report_check_running(ctx):
    cmd = ["ps", "-C", "glusterd"]
    try:
        command_output(cmd)
        ctx.ok("Glusterd is running")
    except CommandError as e:
        ctx.notok("Glusterd is not running")
        logging.warn(ctx.lf("Glusterd is not running",
                            error_code=e[0],
                            error=e[1]))
