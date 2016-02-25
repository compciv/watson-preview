from os.path import join, basename
from glob import glob
import json
PICS_DIR = 'pics'
RECOG_DIR = 'responses'


HTML_FILENAME = 'printout.html'
htmlfile = open(HTML_FILENAME, 'w')
htmlfile.write("<html><title>Hello</title><body>")
htmlfile.write("<h1>Hi this is my ibm watson analysis and my name is NOT dan nguyen</h1>")

# for each file in the recog/ directory
for jsonname in glob(join(RECOG_DIR, '*.json')):
    print("Extracting", jsonname)
    j = json.load(open(jsonname))
    # the data response always returns 'images' as a
    # list of dicts, even if there's just one image
    img = j['images'][0]
    # print out the name of the image as a headline
    imgname = img['image']
    htmlfile.write("<h2>%s</h2>" % imgname)


    # the imgname, as Watson has it in the response
    # is just the file's basename...we need to
    # derive the actual filename from PICS_DIR
    # to refer to where it exists in our project folder
    # i.e. pics/myphoto.jpg
    imgfilename = join(PICS_DIR, imgname)
    # write the code for an image
    htmlfile.write('<img src="%s">' % imgfilename)


    # in the 'scores' list, for each item
    # print out the name of the classifier and its score,
    # i.e. make a list
    # classifier and the pct
    htmlfile.write("STUFF")
    htmlfile.write("MORE STUFF")



htmlfile.close()
