import requests
from os.path import join, basename
from os import makedirs
from glob import glob
import json
API_ENDPOINT='https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify'
PICS_DIR = 'pics'
RECOG_DIR = 'responses'
makedirs(RECOG_DIR, exist_ok=True)
CREDS_FILENAME = 'creds_watson_visual.json'
DEFAULT_PARAMS = {
    'version': '2015-12-02'
}
DEFAULT_HEADERS = {
    'Accept': 'application/json'
}

# get my creds
creds = json.load(open(CREDS_FILENAME))
my_username = creds['credentials']['username']
my_password = creds['credentials']['password']
myauth = (my_username, my_password)


for fname in glob(join(PICS_DIR, '*.jpg')):
    print("Testing", fname)
    with open(fname, 'rb') as imgdata:
        mydict = {}
        mydict['images_file'] = (fname, imgdata)
        resp = requests.post(API_ENDPOINT, params=DEFAULT_PARAMS,
                            auth=myauth, headers=DEFAULT_HEADERS,
                            files=mydict)
        # make sure things are OK: 200
        print(resp.status_code)
        oname = join(RECOG_DIR, basename(fname + '.json'))
        print("Writing to:", oname)
        with open(oname, 'w') as o:
            o.write(resp.text)

