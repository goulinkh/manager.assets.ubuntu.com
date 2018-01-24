#! /usr/bin/env python3
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases() # noqa

import os
import sys


if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "assets_manager.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
