#!/usr/bin/env python

import sys
import os

from subprocess import check_call

image = "datawire/shim-app"
image_tag = "1"

full_image_name = "{0}:{1}".format(image, image_tag)

program = os.path.basename(sys.argv[0])


def main(args):
    if len(args) > 1 and args[0] == "update":
        print("performing update")
        # figure this bit out still... talk to scout and download latest image then self-modify this script?
        return

    check_call(["docker", "run", "--rm", "-it", full_image_name] + args[1:])


if __name__ == "__main__":
    main(sys.argv)
