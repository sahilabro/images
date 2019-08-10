#this function will take a jpg path and resize the image
#the root path is same folder as python script
#the path must include extension (i.e. for example /rose.jpg)


import os
import json 

path = 'rose.jpg'
resizeAttribute = '20%'
outputfilename = 'myconvertedimage'
imagefiletype = 'jpg'

def resizeMyImage(path,resizeAttribute,outputfilename, **kwargs):
    '''Takes optional argument of imagefiletype. If not given it will output a jpg file.
        Takes 3 arguments: path, resizeAttribute, outputfilename. And optional argument ^
        '''
    #check for optional argument (if output filetype other than jpg)
    if 'imagefiletype' in kwargs:
        imagefiletype = kwargs['imagefiletype']
    else:
        imagefiletype = 'jpg'
    
    #for debugging if anything goes wrong
    cliOutput = os.system("magick convert %s -resize %s %s"%(path,resizeAttribute,outputfilename+'.'+imagefiletype))
    
    return 'New image is called %s\nIt is situated in the same folder as this script.'%(outputfilename)



def multiImagefromJson(jsonFilePath):
    '''this takes a json file and parses it into our resizeMyImage function. Please note the JSON file must have the following structure:
    {images: 
        [
            {'path': '/path/to/image.jpg', 'resizeAttribute': '30%', 'outputfilename': 'myNewFile', 'imagefiletype': 'png'},
            {'path': '/path/to/2ndimage.jpg', 'resizeAttribute': '370%', 'outputfilename': 'my2ndNewFile'}
        ]
    }
    the imagefiletype is optional. It will output jpg if not given.
    ' replaced with " as they are not interchangeable in JSON. 
    '''
    #First things first. Open the file and load it into python dictionary:
    with open(jsonFilePath, 'r') as f:
        imagesTobeParsed = json.load(f)

    print(imagesTobeParsed)
    for image in imagesTobeParsed['images']:
        imagefiletype = 'jpg' if 'imagefiletype' not in image else image['imagefiletype']
        resizeMyImage(image['path'],image['resizeAttribute'],image['outputfilename'],imagefiletype='.'+imagefiletype)
 
print(multiImagefromJson('json.json'))