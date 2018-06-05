# speed.cd
A python api for speed.cd

A Python API for interfacing with speed.cd

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
Your rss key is the string folowed by the '='.

getInfo gets information on the torrent (semi working)

getTorrent gets the torrent file (working)

getFreeleech gets a list of the current freeleech torrent IDs (working)
