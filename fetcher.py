import requests
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)

URLS = # HOWEVER YOU CHOOSE TO INCLUDE A LIST OF URL STRING LITERALS

for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = # the name of the place you want to save the image to, e.g. in pics/
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)
