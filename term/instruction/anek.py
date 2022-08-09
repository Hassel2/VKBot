# -*- coding: utf-8 -*-

import os
import sys
import random as rnd

script_dir = os.path.dirname( __file__ )
root_dir = os.path.join( script_dir, '..', '..' )
sys.path.append( root_dir )
import config

function_dir = os.path.join( script_dir, '..', 'function' )
sys.path.append( function_dir )
import messages

def anek( event ):
    count = config.vk.wall.get(owner_id=-85443458, count=1)['count'] - 1
    offset = str(rnd.randint(1, count))
    message = config.vk.wall.get(owner_id=-85443458, count=1, offset=offset)['items'][0]['text']
    try:
        while message == '':
            offset = str(rnd.randint(1, count))
            message = config.vk.wall.get(owner_id=-85443458, count=1, offset=offset)['items'][0]['text']
        messages.reply(message, event)
    except Exception as error:
        messages.reply(error, event)
