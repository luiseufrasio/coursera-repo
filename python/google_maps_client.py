import json
import urllib

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter Location: ')
	if len(address) < 1 : break
	
	url = service_url + urllib.urlencode({'sensor':'false', 'address': address})
	print 'URL: ', url
	uh = urllib.urlopen(url)
	data = uh.read()
	
	print 'Retrieved', len(data), 'characters'
	
	try:
		js = json.loads(str(data))
	except:
		js = None
	if 'status' not in js or js['status'] != 'OK':
		print '===========FAILURE==========='
		print data
		continue
	
	print json.dumps(js, indent=4)
	
	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	print 'lat=', lat, 'lng=', lng 
	
	location = js['results'][0]['formatted_address']
	print location