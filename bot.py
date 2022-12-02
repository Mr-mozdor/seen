from rubpy import Client
from random import choice
from asyncio import run
from re import findall
from time import sleep
from datetime import datetime
from colorama import Fore
import rainbowtext, pyfiglet
import os

bot = Client("mopjtnwujldslxsnmrrmgbfqvarpxvmm")
my_post_link = "https://rubika.ir/cenaret/DCJCCCJECJEFBCC"


global get_information
get_information = []
links = []


print(rainbowtext.text(pyfiglet.figlet_format('   SEEN ')))
print(rainbowtext.text(pyfiglet.figlet_format('                ZAN')))
print(rainbowtext.text(pyfiglet.figlet_format('                 DANIEL  ')))
print(rainbowtext.text(pyfiglet.figlet_format('• * • * • * • * • * • * • *•')))

def color(): return choice(["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m", "\033[0;37m", "\033[1;30m", "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m"])

async def main():
    message_information = await bot.getLinkFromAppUrl(my_post_link)
    message_information = message_information.get('link').get('open_chat_data')
    get_information.append(message_information['message_id'])
    get_information.append(message_information['object_guid'])

    linkdonies = await bot.searchGlobalObjects('c0HGkO0951a2f9159b86470742c0b5d0')
    linkdoni_guids = []
    for i in linkdonies: linkdoni_guids.append(i.get('object_guid')); del i
    for channel_guid in linkdoni_guids:
        channel_last_message_id = await bot.getChannelInfo(channel_guid)
        channel_last_message_id = channel_last_message_id.get('data').get('chat').get('last_message_id')
        messages = await bot.getMessagesInterval(channel_guid, channel_last_message_id)
        messages = messages.get('data').get('messages')
        for get_text in messages:
            if get_text.get('type') == 'Text':
                text = get_text.get('text')
                if text != None:
                    group_link = findall(r"https://rubika.ir/joing/\w{32}", text)
                    for link in group_link:
                        if link != '':
                            links.append(link)
                        else: continue
    
    
    counter = 1
    while True:
        for link in links:
            group_information = await bot.joinGroup(link)
            if 'is_valid' in group_information.get('data').keys() and group_information.get('data').get('is_valid') != False:
                group_guid = group_information.get('data').get('group').get('group_guid')
                group_name = group_information.get('data').get('group').get('group_title')
                group_access = group_information.get('data').get('chat_update').get('chat').get('access')
                if 'SendMessages' in group_access:
                    now = datetime.now()
                    forward = await bot.forwardMessages(get_information[1], [get_information[0]], group_guid)
                    if forward != 'This Group has timer':
                        count_seens = forward.get('data').get('message_updates')[0].get('message').get('count_seen')
                        print(f'{color()}  « °•°•°•°•°•°•°•ˢᵉᵉⁿ ᶻᵃⁿ ᵐʳ ᵈⁿⁱᵉˡ°•°•°•°•°•°•°•°•°•° »')
                        print(f'  « Your PoSt FoR To  : {group_name} »')
                        print(f'  « TiMe FoR : {now.hour}:{now.minute}:{now.second} »')
                        print(f'  « NuMbEr FoR : {counter} »')
                        print(f'  « NuMbEr SeeN PoSt : {count_seens} »')
                        print(f'  « Dev : Mr DaNieL » ')
                        counter += 1
                        print(f"""  « °•°•°•°•°•°•°•ˢᵉᵉⁿ ᶻᵃⁿ ᵐʳ ᵈⁿⁱᵉˡ°•°•°•°•°•°•°•°•°•° » \033[0m
                        """)
                        await bot.leaveGroup(group_guid)
                        sleep(0.1)
                        continue
                    else:
                        await bot.leaveGroup(group_guid)
                        sleep(0.1)
                        continue
                else:
                    await bot.leaveGroup(group_guid)
                    sleep(0.1)
                    continue
        else:
            continue


run(main())