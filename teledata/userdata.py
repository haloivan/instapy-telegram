import os
import time
from base64 import b64encode, b64decode
from telegram.ext import Updater, CommandHandler
from configparser import SafeConfigParser

# set main directory
global mainDir
mainDir = '/root/InstaPy/teledata/'


def userDir(bot, update, chat_data):
	userid = ('{}'.format(update.message.chat_id))
	global uDir
	uDir = (mainDir + 'user/' + userid)
	return 0 if not os.path.exists(uDir) else 1


def findConfig(bot, update, chat_data):
	userdirinfo = userDir(bot, update, chat_data)
	if userdirinfo != 0 :
		if not os.path.exists(uDir + '/user'):
			return 0
		elif os.path.exists(uDir + '/user') == True:
			f = open(uDir + '/user', 'r')
			dec = b64decode(f.read())
			wdec = open(uDir + '/config.ini', 'w+')
			wdec.write(dec)
			return True
	else:
		return 0

def getUsername(bot, update, chat_data):
	config = SafeConfigParser()
	config.read(uDir + '/config.ini')
	return config.get('instapy', 'username')


def getPassword(bot, update, chat_data):
	config = SafeConfigParser()
	config.read(uDir + '/config.ini')
	return config.get('instapy', 'password')


class getUserConfig:
	def __init__(self, bot, update, chat_data):
		if findConfig(bot, update, chat_data) == True:
			self.username = getUsername(bot, update, chat_data)
			self.password = getPassword(bot, update, chat_data)
			os.remove(uDir + '/config.ini')
		else:
			return 0


def userConfig(bot, update, chat_data):
	return getUserConfig(bot, update, chat_data)
