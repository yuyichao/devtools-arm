#!/usr/bin/env python

import os
import sys

if 'MAKEFLAGS' in os.environ:
    os.environ['MAKEFLAGS_saved'] = os.environ['MAKEFLAGS']

# Use python so that we can set $0.
os.execvp('archbuild', sys.argv)
