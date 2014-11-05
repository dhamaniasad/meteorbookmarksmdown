import requests
import html2text
import filecmp
import os
from apscheduler.schedulers.background import BackgroundScheduler
import time


def run():
    r = requests.get("http://gillesfabio.github.io/meteor-bookmarks/")
    h = html2text.HTML2Text()
    h.ignore_images = True
    s = r.text.encode('ascii', 'ignore').decode('ascii')
    mdown = h.handle(s)
    f3 = open('sourcediff.md', 'w+')
    print >> f3, mdown
    f3.close()
    if filecmp.cmp('sourcediff.md', 'source.md') is False:
        os.remove('source.md')
        f2 = open('source.md', 'w+')
        print >> f2, mdown
    os.remove('sourcediff.md')

apsched = BackgroundScheduler()
apsched.add_job(run, 'interval', seconds=86400)
apsched.start()

while True:
    time.sleep(86000)
