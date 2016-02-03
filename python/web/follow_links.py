import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
total_count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))

count = 1
while count <= total_count:
    count += 1
    print 'Retrieving: %s' % url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    a = soup('a')[pos-1]
    url = a['href']

print 'Last Url: %s' % url