import speedcd
import sys

# Gets the list of current freeleeches, downloads if not already in log
log = ''
try:
	log = sys.argv[1]
except Exception:
	print('Error: No log file specified')
	exit()

try:
	output = sys.argv[2]
except Exception:
	print('Error: Torrent file location specified')
	exit()

# Fill in credentials for speed
creds = {'username': 'USERNAMEHERE', 'password': 'PASSWORDHERE', 'key':'FREELEECHKEYHERE'}

# Get freeleech list
freeList = speedcd.getFreeleech(creds)

# Get content os log (torrents already grabbed)
try:
	file_object = open(log,'r')
except Exception:
	# There is most likley no file, we will generate the file for fist time use
	file_object = open(log,'w+')
	for torrent in freeList:
		file_object.write(str(torrent) + '\r\n')
	file_object.close()
	print('log file created, run again to begin watch')
	exit()

# Get already logged torrents
logged = [int(line.rstrip('\n')) for line in file_object]
file_object.close()

# IF there is a new freeleech, download it
for freeItem in freeList:
	if int(freeItem) not in logged:
		print('Torrent ' + str(freeItem) + ' not found, downloading')
		try:
			speedcd.getTorrent(creds, freeItem, str(output))
			with open(log, 'a') as the_file:
				the_file.write(str(freeItem) + '\n')
			the_file.close()
		except Exception:
			print('Error: Unable to download torrent for ' + str(freeItem))

