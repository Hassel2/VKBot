# -*- coding: utf-8 -*-

import os
import sys

script_dir = os.path.dirname( __file__ )
root_dir = os.path.join( script_dir, '..' )
sys.path.append( root_dir )
import config
import admins
import blacklist

import instruction.say_hi as say_hi
import instruction.anek as anek
import instruction.cit_gen as cit_gen

def route( event, instruction_args ):

    if instructions[instruction_args[0]]['admin'] and event.user_id not in admins.admins_list:
        return False
    if instructions[instruction_args[0]]['blacklist'] and event.user_id in blacklist.blacklist:
        return False

    instructions[instruction_args[0]]['instruction']( event );



instructions = {
    'привет' : {
        'instruction' : say_hi.say_hi,
        'blacklist'   : False,
        'admin'       : False,
    },
    'анек'   : {
        'instruction' : anek.anek,
        'blacklist'   : False,
        'admin'       : False,
    },
    'цитген'   : {
        'instruction' : cit_gen.cit_gen,
        'blacklist'   : False,
        'admin'       : False,
    },
}
