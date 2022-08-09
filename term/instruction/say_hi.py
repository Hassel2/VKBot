# -*- coding: utf-8 -*-

import os
import sys
from vk_api.utils import get_random_id

script_dir = os.path.dirname( __file__ )
root_dir = os.path.join( script_dir, '..', '..' )
sys.path.append( root_dir )
import config

def say_hi(event):
    config.vk.messages.send(
        random_id = get_random_id(),
        peer_id = event.peer_id,
        message = 'Hello world',
        reply_to = event.message_id
    )
