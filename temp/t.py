
from BeautifulSoup import BeautifulSoup as BS
import urllib2

url = "http://www.52nlp.cn/"
html = urllib2.urlopen(url).read()

bs = BS(html)

print bs

