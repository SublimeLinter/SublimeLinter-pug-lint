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

from SublimeLinter.lint import Linter, util


class JadeLint(Linter):

    """Provides an interface to jade-lint."""

    syntax = 'jade'
    cmd = 'jade-lint'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0.2'
    regex = r''
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

