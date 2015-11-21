#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ben Edwards
# Copyright (c) 2015 Ben Edwards
#
# License: MIT
#

"""This module exports the JadeLint plugin class."""

from SublimeLinter.lint import NodeLinter, util, highlight

class JadeLint(NodeLinter):

    """Provides an interface to jade-lint."""

    npm_name = 'jade-lint'
    syntax = 'jade'
    cmd = 'jade-lint @ *'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.0.0'
    regex = r'^.+?:(?P<line>\d+)(:(?P<col>\d+) | )(?P<message>.+)'
    multiline = False
    tempfile_suffix = 'jade'
    error_stream = util.STREAM_BOTH
    config_file = ('--config', '.jade-lintrc', '.jade-lint.json', '~')
    defaults = {'--reporter=': 'inline'}
    default_type = highlight.WARNING
