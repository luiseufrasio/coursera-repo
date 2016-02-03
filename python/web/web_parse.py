import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
count = 0
total = 0
for tag in tags:
    count += 1
    total += int(tag.contents[0])

print 'Count %d' % count
print 'Sum %d' % total