# !/usr/bin/env python
# -*- encoding: utf-8, -*-

# Program ini dikembangkan dari
# InstaPy https://github.com/timgrossmann/InstaPy
# InstaPy Telegram Bot https://github.com/Tkd-Alex/Telegram-InstaPy-Scheduling
# Edited By SkyJackerz

import unicodedata
import logging
import threading
import time
import json
import datetime
import random
import sys
import os

from instatelemod import setting, skipmod, langmod
from telegram.ext import Updater, CommandHandler, Job, CallbackQueryHandler
from instapy import InstaPy
from configparser import SafeConfigParser
from pprint import pprint

# Folder
global directory
dirutama = setting.dirutama()
directory = (dirutama + '/teledata/')
if not os.path.exists(directory):
    os.makedirs(directory)


# Get instagram data from config.ini
config = SafeConfigParser()
config.read(directory+'config.ini')
telegram_token = config.get('telegram', 'token')
insta_username = config.get('instapy', 'username')
insta_password = config.get('instapy', 'password')


def help(bot, update):
    update.message.reply_text(langmod.pesan('help', 'help'))


def feed(bot, update, args):
    try:
        data = {'data': args[0]}
        chat_data = data
        dFeed = chat_data['data']

        if dFeed > '0' and dFeed != '':
            update.message.reply_text(langmod.pesan('feed', 'main'))
            start = datetime.datetime.now().replace(microsecond=0)
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              nogui=True)
            session.login()
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=1000000000,
                                            max_following=10000,
                                            min_followers=30,
                                            min_following=25)
            session.set_do_comment(False, percentage=10)
            session.set_dont_like(skipmod.banfile())
            session.like_by_feed(amount=int(dFeed),
                                 randomize=False,
                                 unfollow=False,
                                 interact=False)
            session.end()
            with open('/root/InstaPy/logs/general.log', "r") as f:
                      f.seek (0, 2) 
                      fsize = f.tell()
                      f.seek (max (fsize-1024, 0), 0)
                      lines = f.readlines()

            lines = lines[-9:]
            ctlog = datetime.datetime.now().replace(microsecond=0)
            tgllog = ('{}'.format(ctlog))
            rlog = ''.join(x.replace('[', '')
                     .replace(']', '')
                     .replace('INFO ', '')
                     .replace(' ', '/')
                     .replace('//', '#')
                     .replace('/', ' ')
                     .replace('#', '')
                     .replace(tgllog, '')
                     .replace(insta_username, '') for x in lines)
            end = datetime.datetime.now().replace(microsecond=0)
            endmessage = ('InstaBot feed liker selesai {}'
                          .format(time.strftime("%X")))
            update.message.reply_text(endmessage + '\n' +
                                      'Report Log:\n' +
                                      rlog +
                                      'Durasi Eksekusi {}'
                                      .format(end-start))
        elif dFeed == 'help':

            update.message.reply_text(langmod.pesan('feed', 'help'))

    except (IndexError, ValueError):
        update.message.reply_text(langmod.pesan('feed', 'help'))


def tag(bot, update, args):
    try:

        data = {'tags': args[0], 'like': args[1]}
        chat_data = data
        tags = chat_data['tags']
        like = chat_data['like']

        if tags == 'help':
            update.message.reply_text(langmod.pesan('tag', 'help'))

        elif tags != 'auto' and like > '0':

            update.message.reply_text(langmod.info('tag', 'main', tags, like))
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              nogui=True)
            start = datetime.datetime.now().replace(microsecond=0)
            session.login()
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=1000000000,
                                            max_following=10000,
                                            min_followers=30,
                                            min_following=25)
            session.set_do_comment(False, percentage=10)
            session.set_dont_like(skipmod.banfile())
            session.like_by_tags([tags], amount=int(like))
            session.end()
            with open('/root/InstaPy/logs/general.log', "r") as f:
                f.seek (0, 2)                   # Seek @ EOF
                fsize = f.tell()                # Get Size
                f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
                lines = f.readlines()           # Read to end

            lines = lines[-9:]                  # Get last 10 lines
            ctlog = datetime.datetime.now().replace(microsecond=0)
            tgllog = ('{}'.format(ctlog))
            rlog = ''.join(x.replace('[', '')
                     .replace(']', '')
                     .replace('INFO ', '')
                     .replace(' ', '/')
                     .replace('//', '#')
                     .replace('/', ' ')
                     .replace('#', '')
                     .replace(tgllog, '')
                     .replace(insta_username, '') for x in lines)
            end = datetime.datetime.now().replace(microsecond=0)
            endmessage = ('InstaBot tag liker selesai {}'
                          .format(time.strftime("%X")))
            update.message.reply_text(endmessage + '\n' +
                                      'Report Log:\n' +
                                      rlog +
                                      'Durasi Eksekusi {}'
                                      .format(end-start))

        elif tags == 'auto' and like > '0':
            update.message.reply_text('menyukai tagar secara automatis '
                                      'paling banyak ' + like +
                                      ' like tiap tagar.')
            tag_1 = ['x', 'x', 'x', 'x', 'x']
            tag_2 = ['x', 'x', 'x', 'x', 'x']
            tag_3 = ['x', 'x', 'x', 'x', 'x']
            tag_4 = ['x', 'x', 'x', 'x', 'x']
            random.seed(time.time())
            xtag = ['#'+tag_1[random.randint(0, len(tag_1)-1)],
                    '#'+tag_2[random.randint(0, len(tag_2)-1)],
                    '#'+tag_3[random.randint(0, len(tag_3)-1)],
                    '#'+tag_4[random.randint(0, len(tag_4)-1)]]
            random.shuffle(xtag)
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              nogui=True)
            start = datetime.datetime.now().replace(microsecond=0)
            session.login()
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=1000000000,
                                            max_following=10000,
                                            min_followers=30,
                                            min_following=25)
            session.set_do_comment(False, percentage=10)
            session.set_dont_like(skipmod.banfile())
            update.message.reply_text('menyukai tagar ' + xtag[0])
            session.like_by_tags([xtag[0]], amount=int(like), interact=False)
            session.end()
            with open('/root/InstaPy/logs/general.log', "r") as f:
                f.seek (0, 2)                   # Seek @ EOF
                fsize = f.tell()                # Get Size
                f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
                lines = f.readlines()           # Read to end

            lines = lines[-9:]                  # Get last 10 lines
            ctlog = datetime.datetime.now().replace(microsecond=0)
            tgllog = ('{}'.format(ctlog))
            rlog = ''.join(x.replace('[', '')
                     .replace(']', '')
                     .replace('INFO ', '')
                     .replace(' ', '/')
                     .replace('//', '#')
                     .replace('/', ' ')
                     .replace('#', '')
                     .replace(tgllog, '')
                     .replace(insta_username, '') for x in lines)
            update.message.reply_text('Report Log:\n' +
                                      rlog +
                                      '>> menyukai tagar ' + xtag[1] + 
                                      ' tunggu sebentar...')
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              nogui=True)
            session.login()
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=1000000000,
                                            max_following=10000,
                                            min_followers=30,
                                            min_following=25)
            session.set_do_comment(False, percentage=10)
            session.set_dont_like(skipmod.banfile())
            update.message.reply_text('menyukai tagar ' + xtag[1])
            session.like_by_tags([xtag[1]], amount=int(like), interact=False)
            session.end()
            with open('/root/InstaPy/logs/general.log', "r") as f:
                f.seek (0, 2)                   # Seek @ EOF
                fsize = f.tell()                # Get Size
                f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
                lines = f.readlines()           # Read to end

            lines = lines[-9:]                  # Get last 10 lines
            ctlog = datetime.datetime.now().replace(microsecond=0)
            tgllog = ('{}'.format(ctlog))
            rlog = ''.join(x.replace('[', '')
                     .replace(']', '')
                     .replace('INFO ', '')
                     .replace(' ', '/')
                     .replace('//', '#')
                     .replace('/', ' ')
                     .replace('#', '')
                     .replace(tgllog, '')
                     .replace(insta_username, '') for x in lines)
            update.message.reply_text('Report Log:\n' +
                                      rlog +
                                      '>> menyukai tagar ' + xtag[2] + 
                                      ' tunggu sebentar...')
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              nogui=True)
            session.login()
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=1000000000,
                                            max_following=10000,
                                            min_followers=30,
                                            min_following=25)
            session.set_do_comment(False, percentage=10)
            session.set_dont_like(skipmod.banfile())
            update.message.reply_text('menyukai tagar ' + xtag[2])
            session.like_by_tags([xtag[2]], amount=int(like), interact=False)
            session.end()
            with open('/root/InstaPy/logs/general.log', "r") as f:
                f.seek (0, 2)                   # Seek @ EOF
                fsize = f.tell()                # Get Size
                f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
                lines = f.readlines()           # Read to end

            lines = lines[-9:]                  # Get last 10 lines
            ctlog = datetime.datetime.now().replace(microsecond=0)
            tgllog = ('{}'.format(ctlog))
            rlog = ''.join(x.replace('[', '')
                     .replace(']', '')
                     .replace('INFO ', '')
                     .replace(' ', '/')
                     .replace('//', '#')
                     .replace('/', ' ')
                     .replace('#', '')
                     .replace(tgllog, '')
                     .replace(insta_username, '') for x in lines)
            update.message.reply_text('Report Log:\n' +
                                      rlog +
                                      '>> menyukai tagar ' + xtag[3] + 
                                      ' tunggu sebentar...')
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              nogui=True)
            session.login()
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=1000000000,
                                            max_following=10000,
                                            min_followers=30,
                                            min_following=25)
            session.set_do_comment(False, percentage=10)
            session.set_dont_like(skipmod.banfile())
            update.message.reply_text('menyukai tagar ' + xtag[3])
            session.like_by_tags([xtag[3]], amount=int(like), interact=False)
            session.end()
            with open('/root/InstaPy/logs/general.log', "r") as f:
                f.seek (0, 2)                   # Seek @ EOF
                fsize = f.tell()                # Get Size
                f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
                lines = f.readlines()           # Read to end

            lines = lines[-9:]                  # Get last 10 lines
            ctlog = datetime.datetime.now().replace(microsecond=0)
            tgllog = ('{}'.format(ctlog))
            rlog = ''.join(x.replace('[', '')
                     .replace(']', '')
                     .replace('INFO ', '')
                     .replace(' ', '/')
                     .replace('//', '#')
                     .replace('/', ' ')
                     .replace('#', '')
                     .replace(tgllog, '')
                     .replace(insta_username, '') for x in lines)
            end = datetime.datetime.now().replace(microsecond=0)
            endmessage = ('InstaBot tag liker selesai {}'
                          .format(time.strftime("%X")))
            update.message.reply_text(endmessage + '\n' +
                                      'Report Log:\n' +
                                      rlog +
                                      'Durasi Eksekusi {}'
                                      .format(end-start))
    except (IndexError, ValueError):
        update.message.reply_text(helpmessage)


def user(bot, update, args):
    query = update.callback_query
    try:
        data = {'userig': args[0], 'like': args[1]}
        chat_data = data
        userig = chat_data['userig']
        like = chat_data['like']

        if userig == 'help':
            update.message.reply_text(langmod.pesan('user', 'help'))

        elif userig != '' and like > '0':
            update.message.reply_text(langmod.info('user', 'info', userig, like))
            start = datetime.datetime.now().replace(microsecond=0)
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              nogui=True)
            session.login()
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=1000000000,
                                            max_following=10000,
                                            min_followers=30,
                                            min_following=25)
            session.set_do_comment(False, percentage=10)
            session.set_dont_like(skipmod.banfile())
            session.set_do_like(True, percentage=100)
            session.interact_by_users([userig],
                                      amount=int(like),
                                      randomize=False)
            session.end()
            with open('/root/InstaPy/logs/general.log', "r") as f:
                f.seek (0, 2)                   # Seek @ EOF
                fsize = f.tell()                # Get Size
                f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
                lines = f.readlines()           # Read to end

            lines = lines[-9:]                  # Get last 10 lines
            ctlog = datetime.datetime.now().replace(microsecond=0)
            tgllog = ('{}'.format(ctlog))
            rlog = ''.join(x.replace('[', '')
                     .replace(']', '')
                     .replace('INFO ', '')
                     .replace(' ', '/')
                     .replace('//', '#')
                     .replace('/', ' ')
                     .replace('#', '')
                     .replace(tgllog, '')
                     .replace(insta_username, '') for x in lines)
            end = datetime.datetime.now().replace(microsecond=0)
            endmessage = ('InstaBot user liker selesai {}'
                          .format(time.strftime("%X")))
            update.message.reply_text(endmessage + '\n' +
                                      'Report Log:\n' +
                                      rlog +
                                      'Durasi Eksekusi {}'
                                      .format(end-start))

    except (IndexError, ValueError):
        update.message.reply_text(langmod.pesan('user', 'help'))


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(telegram_token)

    ud = updater.dispatcher

    ud.add_handler(CommandHandler('start', help))
    ud.add_handler(CommandHandler('help', help))

    ud.add_handler(CommandHandler('feed', feed, pass_args=True))
    ud.add_handler(CommandHandler('tag', tag, pass_args=True))
    ud.add_handler(CommandHandler('user', user, pass_args=True))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
