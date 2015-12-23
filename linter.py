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

    npm_name = 'pug-lint'
    syntax = 'pug'
    cmd = 'pug-lint @ *'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.1.1'
    regex = r'^.+?:(?P<line>\d+)(:(?P<col>\d+) | )(?P<message>.+)'
    multiline = False
    tempfile_suffix = 'pug'
    error_stream = util.STREAM_BOTH
    config_file = ('--config', '.pug-lintrc', '.pug-lint.json', '.jade-lintrc', '.jade-lint.json', '~')
    defaults = {'--reporter=': 'inline'}
    default_type = highlight.WARNING
