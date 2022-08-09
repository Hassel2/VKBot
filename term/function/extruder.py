# -*- coding: utf-8 -*-

import os
import sys
import re

script_dir = os.path.dirname( __file__ )
root_dir = os.path.join( script_dir, '..', '..' )
sys.path.append( root_dir )
import config

router_dir = os.path.join( script_dir, '..' )
sys.path.append( router_dir )
import router

def extrude( event ):
    message = re.sub(r'\s+', ' ', event.text)
    if message[0] != config.prefix:
        return False
    messageArg = message[1:].split(' ')
    messageArg[0] = messageArg[0].lower()
    router.route(event, messageArg)

