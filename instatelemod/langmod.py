from instatelemod import setting
from configparser import SafeConfigParser

class getlang:
	def __init__(self, comm, mVal):
		dirutama = setting.dirutama()
		lang = SafeConfigParser()
		lang.read(dirutama+'/instatelemod/lang/id_ID.ini')
		msg = lang.get(comm, mVal)
		self.msg = msg


def pesan(comm, mVal):
	lang = getlang(comm, mVal)
	message = (lang.msg)
	return message


def info(comm, mVal, fVal, sVal):
	f = fVal
	s = sVal
	lang = getlang(comm, mVal)
	msg = lang.msg
	message = (msg + f + ' paling banyak ' + s + ' like.')
	return message
