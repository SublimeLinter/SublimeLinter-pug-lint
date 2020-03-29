#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ben Edwards
# Copyright (c) 2015 Ben Edwards
#
# License: MIT
#

"""This module exports the PugLint plugin class."""

from SublimeLinter.lint import NodeLinter, util, highlight


class PugLint(NodeLinter):
    """Provides an interface to pug-lint."""

    cmd = 'pug-lint @ *'
    regex = r'^.+?:(?P<line>\d+)(:(?P<col>\d+) | )(?P<message>.+)'
    multiline = False
    tempfile_suffix = 'pug'
    error_stream = util.STREAM_BOTH
    defaults = {
        'selector': 'text.pug, source.pypug, text.jade',
        '--reporter=': 'inline'
    }
    default_type = highlight.WARNING
