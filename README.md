# speed.cd
A Python3 API for interfacing with speed.cd

## Setup

### Install
Download speedcd.py and move to your dist-packages directory.

For linux:
```
cp speedcd.py /usr/lib/python3/dist-packages/
```
For Windows:
```
idk
```
For Mac:
```
idk
```

### Credentials
Credential JSON has the following format:
```
{
	'username': '[speed.cd username]',
	'password': '[speed.cd password]',
	'key':'[rss key]'
}
```
Your rss key can be found by clicking on RSS, selecting any catagory, and selecting the 'download link' radio button. At this point a url should have been generated in the text box above these selections. A section of the url has the format 
```
passkey=xxx......xxx
```
Your rss key is the string folowed by the '='

## Functions
getInfo gets information on the torrent (semi working)

getTorrent gets the torrent file (working)

getFreeleech gets a list of the current freeleech torrent IDs (working)

## Uses
I have some working examples of uses for the API

The first one is an automatic freeleech grabber. When ran for the first time it generates a list of the current freeleech torrents. Every time it is ran after that, if there is a new freeleech it is added to the list and downloaded

Pass in the log file and location for storing torrent files
```
python3 freeleech.py logfile.txt /home/bobby/marry
```
