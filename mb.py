import requests
import html2text
import filecmp

r = requests.get("http://gillesfabio.github.io/meteor-bookmarks/")
h = html2text.HTML2Text()
h.ignore_images = True
s = r.text.encode('ascii', 'ignore').decode('ascii')
mdown = h.handle(s)
f3 = open('sourcediff.mdown', 'w+')
print >> f3, mdown
with open('sourcediff.mdown') as no2:
    s2 = no2.read()
with open('source.mdown') as no1:
    s1 = no1.read()
if s2 == s1:
    pass
else:
    print "Different"
"""
f2 = open('source.mdown', 'w+')
print >> f2, mdown
"""