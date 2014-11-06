import requests
import html2text
import filecmp
import os
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging


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
        gistkey = os.environ.get('GITHUBGISTKEY')
        headers = {'Authorization': 'token %s' % (gistkey),
        'User-Agent': 'dhamaniasad'}
        data = {"description":"",
        "files": {
        "meteorbookmarks.md": {
        "content": "%s" % (mdown)
        }
        }}
        listgist = requests.patch("https://api.github.com/gists/646c4c4a3faec7616976", headers=headers, json=data)
        print listgist.text
    os.remove('sourcediff.md')

logging.basicConfig()
apsched = BackgroundScheduler()
apsched.add_job(run, 'interval', seconds=5)
apsched.start()

while True:
    time.sleep(3)
