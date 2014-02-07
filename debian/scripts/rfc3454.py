#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-

# $Id: rfc3454.py 22551 2008-02-01 16:22:22Z lha $

# Copyright (c) 2004 Kungliga Tekniska H�gskolan
# (Royal Institute of Technology, Stockholm, Sweden). 
# All rights reserved. 
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions 
# are met: 
# 
# 1. Redistributions of source code must retain the above copyright 
#    notice, this list of conditions and the following disclaimer. 
# 
# 2. Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in the 
#    documentation and/or other materials provided with the distribution. 
# 
# 3. Neither the name of the Institute nor the names of its contributors 
#    may be used to endorse or promote products derived from this software 
#    without specific prior written permission. 
# 
# THIS SOFTWARE IS PROVIDED BY THE INSTITUTE AND CONTRIBUTORS ``AS IS'' AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED.  IN NO EVENT SHALL THE INSTITUTE OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS 
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY 
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF 
# SUCH DAMAGE. 

import re
import string

def read(filename):
    """return a dict of tables from rfc3454"""
    f = open(filename, 'r')
    inTable = False
    while True:
        l = f.readline()
        if not l:
            break
        if inTable:
            m = re.search('^[a-zA-Z]', l)
            if not m:
                    print l

            m = re.search('^ *----- End Table ([A-Z0-9\.]+) ----- *$', l)
            if m:
                inTable = False

        if re.search('^ *----- Start Table ([A-Z0-9\.]+) ----- *$', l):
            print l
            inTable = True
    f.close()
    return

import sys

if len(sys.argv) != 2:
    print "usage: %s rfc3454.txt" % sys.argv[0]
    sys.exit(1)

tables = read(sys.argv[1])
