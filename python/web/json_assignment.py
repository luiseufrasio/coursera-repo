import json
import urllib

while True:
	address = raw_input('Enter Location: ')
	if len(address) < 1 : break
	
	uh = urllib.urlopen(address)
	data = uh.read()
	
	try:
		js = json.loads(str(data))
	except:
		js = None
	if 'note' not in js:
		print '===========FAILURE==========='
		print data
		continue
	
	count = 0
	for comment in js['comments']:
		count += int(comment['count'])
		
	print count