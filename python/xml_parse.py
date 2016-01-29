import urllib
import xml.etree.ElementTree as ET

url = raw_input('URL: ')

xml_text = urllib.urlopen(url).read()
xml_obj = ET.fromstring(xml_text)

result = 0
comments = xml_obj.find('comments').findall('comment')
for comment in comments:
    result += int(comment.find('count').text)

print result