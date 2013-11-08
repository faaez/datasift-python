# encoding: utf-8

"""
The official DataSift API library for Python. This module provides access to
the REST API and also facilitates consuming streams.

Requires Python 2.4+.

To use, 'import datasift' and create a datasift.User object passing in your
username and API key. See the examples folder for reference usage.

Source Code:

https://github.com/datasift/datasift-python

Examples:

https://github.com/datasift/datasift-python/tree/master/examples

DataSift Platform Documentation:

http://dev.datasift.com/docs/

Copyright (C) 2012 MediaSift Ltd. All Rights Reserved.

This software is Open Source. Read the license:

https://github.com/datasift/datasift-python/blob/master/LICENSE
"""
import sys
import os

__author__ = "Courtney Robinson <courtney.robinson@datasift.com>"
__status__ = "beta"
__version__ = "1.0.0"
__date__ = "1st Nov 2013"

#-----------------------------------------------------------------------------
# Add this folder to the system path.
#-----------------------------------------------------------------------------
sys.path[0:0] = [os.path.dirname(__file__), ]

#-----------------------------------------------------------------------------
# Module constants
#-----------------------------------------------------------------------------
USER_AGENT = 'DataSiftPython/%s' % __version__
API_HOST = 'api.datasift.com/'

#-----------------------------------------------------------------------------
# Check for SSL support.
#-----------------------------------------------------------------------------
try:
    import ssl
except ImportError:
    SSL_AVAILABLE = False
else:
    SSL_AVAILABLE = True

from client import Client as DataSiftClient