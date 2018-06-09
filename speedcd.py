import requests, time, string, random
from bs4 import BeautifulSoup

# Collects general information on a torrent, given the torrent id
def getInfo(creds, torrent):
	time.sleep(3)
	# Get torrent page
	loginURL = 'https://speed.cd/take.login.php'
	html = ''
	with requests.Session() as session:
		post = session.post(loginURL,data=creds)
		r = session.get('https://speed.cd/t/' + str(torrent))
		html = r.text
	# Load into beautifulsoup
	page = BeautifulSoup(html, 'html.parser')
	# Find name
	name = page.find('h3', {'id':'boxTitle'}).text
	# Get info bar
	infoBar = page.find('div', {'class':'infoHead nfo'}).find_all('span')
	# Get Size
	size = str(infoBar[0]).split('Size"/> ',1)[1][:-7]
	# Get seeders
	seeders = str(infoBar[1]).split('<b>',1)[1][:-15]
	# Get leechers
	leechers = str(infoBar[2]).split('<b>',1)[1][:-15]
	# Get snatchers
	snatched = str(infoBar[3]).split('Snatched"/> ',1)[1][:-7]
	# Get upload date
	uploaded = str(infoBar[4]).split('Date" title="',1)[1].split('">',1)[0]
	# Get catagory
	catagory = str(infoBar[6]).split('blank">',1)[1][:-11]
	# Get uploader
	uploader = 'Anonymous'
	if '<b>' in str(infoBar[7]):
		# Not anon uploader
		uploader = str(infoBar[7]).split('<b>',1)[1][:-15]
	# Get files
	files = str(infoBar[8]).split('Files">',1)[1][:-17]
	# Data dict
	data = {'name':name, 'size':size, 'seeders':seeders, 'leechers':leechers, 'snatched':snatched, 'uploaded':uploaded, 'catagory':catagory, 'uploader':uploader, 'files':files}
	return data

# Downloads the torrent file for a torrent, given the torrent id
def getTorrent(creds, torrent, destination):
	# Get Torrent Name
	try:
		name = getInfo(creds, torrent)['name']
	except Exception:
		print('Error: Problems getting torrent info, saving as torrent id')
		name = str(torrent)
	# Log in
	loginURL = 'https://speed.cd/take.login.php'
	html = ''
	with requests.Session() as session:
		post = session.post(loginURL,data=creds)
		# Must include key from  rss feed to be able to download
		r = session.get('https://speed.cd/download.php?torrent=' + str(torrent) + '&key=' + creds['key'])
		with open(destination + '/' + name + '.torrent','wb') as code:
			code.write(r.content)

# Gets a list of the current freeleech torrents
def getFreeleech(creds):
	# Fetch the freeleech page
	loginURL = 'https://speed.cd/take.login.php'
	freeleechPage = 'https://speed.cd/browse.php?freeleech=on'
	html = ''
	with requests.Session() as session:
		post = session.post(loginURL,data=creds)
		r = session.get(freeleechPage)
		html = r.text
	# Load into bs
	page = BeautifulSoup(html, 'html.parser')
	# Get box of freeleech torrents
	box = page.find('div', {'class':'boxContent'})
	# Get each torrent in the list
	freeleech = box.find_all('tr')
	iterator = iter(freeleech)
	next(iterator)
	prev = next(iterator)
	theList = []
	for free in iterator:
		theList.append(int(str(prev).split('"tr',1)[1].split('"',1)[0]))
		prev = free
	return theList
