# -*- coding: utf-8 -*-

import config
import vk_api
import sys
import os 
from vk_api.longpoll import VkLongPoll, VkEventType


if __name__ == "__main__":
    if not os.path.isfile(f"term/command/{sys.argv[1]}.py"):
        raise Exception(f"No command name {sys.argv[1]} was specified")
    os.system(f"python3 term/command/{sys.argv[1]}.py")
