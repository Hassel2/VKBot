# -*- coding: utf-8 -*-

import os
import sys
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

script_dir = os.path.dirname( __file__ )
root_dir = os.path.join( script_dir, '..', '..' )
sys.path.append( root_dir )
import config

function_dir = os.path.join( script_dir, '..', 'function' )
sys.path.append( function_dir )
import extruder



def main():
    # try:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text:
            print(extruder.extrude(event))

    # except Exception as error:
    #     print(error)
    #     main()


if __name__ == "__main__":

    vk_session = vk_api.VkApi(token = config.token, app_id = config.app_id )
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    config.vk = vk

    main()


