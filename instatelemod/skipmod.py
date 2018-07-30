from instatelemod import setting

dirutama = setting.dirutama()

def banfile():
	file = []
	with open(dirutama+'/teledata/banlist.txt') as f:
		for line in f:
			file.append(line.strip("\n").replace('\r', ''))
	return file
