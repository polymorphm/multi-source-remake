#!/usr/bin/env python
#-*- coding: utf-8 -*-
# for Python-2.6:
from __future__ import absolute_import, division, print_function, unicode_literals

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without_path even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, locale

from .safe_unicode import safe_unicode

def get_app_name():
    # get encoding or 'None'
    encoding = locale.getdefaultlocale()[1]
    # get first arg as bytes in system encoding
    app_name_b = sys.argv[0]
    
    app_name = safe_unicode(
        app_name_b,
        encoding=encoding,
    )
    
    return app_name

def get_args():
    # get encoding or 'None'
    encoding = locale.getdefaultlocale()[1]
    # get args as bytes in system encoding
    args_b = sys.argv[1:]
    
    args = [
        safe_unicode(
            arg_b,
            encoding=encoding,
        )
        for arg_b in args_b
    ]
    
    return args


