# -*- coding: utf-8 -*-

import os
import sys
import textwrap
import requests
from PIL import Image, ImageDraw, ImageFont

script_dir = os.path.dirname( __file__ )
root_dir = os.path.join( script_dir, '..', '..' )
sys.path.append( root_dir )
import config

function_dir = os.path.join( script_dir, '..', 'function' )
sys.path.append( function_dir )
import messages


def cit_gen( event ):
    message_items = config.vk.messages.getById(message_ids = event.message_id)['items'][0]

    # Get information
    if 'reply_message' in message_items:
        user_id = message_items['reply_message']['from_id']
        text = '«' + message_items['reply_message']['text'] + '»'
    elif len(message_items['fwd_messages']) != 0:
        user_id = message_items['fwd_messages'][0]['from_id']
        text = ''
        for fwd_message in message_items['fwd_messages']:
            if user_id != fwd_message['from_id']:
                return
            text += '-' + fwd_message['text'] + '\n'
    else:
        return
       
    user_info = config.vk.users.get(user_ids=user_id, fields = 'photo_200')
    first_name = user_info[0]['first_name']
    last_name = user_info[0]['last_name']
    photo_url = user_info[0]['photo_200']
    full_name = '© ' + first_name + ' ' + last_name

    height = 350
    width = 1040
    splited_text = text.split(sep = '\n')
    formated_text = []
    for i in splited_text:
        formated_text += textwrap.wrap(i, width=40, break_long_words=True)

    if len(formated_text) > 4:
        height = 37 + 40 * (len(formated_text)) + 137

    text = "\n".join(formated_text)

    resp = requests.get(photo_url, stream=True).raw
    photo = Image.open(resp)
    img = Image.new('RGBA', (1040, height), 'black')
    img.paste(photo, (30, 30))
    idraw = ImageDraw.Draw(img)
    iosevka = ImageFont.truetype(root_dir + '/src/fonts/iosevka.ttf', size=36)
    idraw.rectangle((10, 10, 1030, height - 100))


    # margin = 270
    # offset = 23
    # for line in formated_text:
    #     idraw.text((margin, offset), line, font=font)
    #     offset += font.getsize(line)[1]

    idraw.multiline_text((270, 23), text, font=iosevka, spacing=5)
    idraw.text((936 - len(full_name) * 16, height - 155), full_name, font=iosevka)

    tnm = ImageFont.truetype(root_dir + '/src/fonts/times-new-roman.ttf', size = 72)
    idraw.text((112, height - 89),'ЗОЛОТОЙ ФОНД ЦИТАТ', font=tnm)

    img.save(root_dir + '/src/cit.png')
    img.close()
    photo.close()

