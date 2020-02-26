###necessary Librarie to work with
import os
from pathlib import Path

#######Map file extension to our needs for sorting
subdirectories = {
    "DOCS" : ['.pdf','.csv','.txt','.sql'],
    "AUDIOS" : ['.m4a','.mp3'],
    "VIDEOS" : ['.avi','.mp4','.mkv','.mov'],
    "IMAGES" : ['.jpg','.png',',jpeg']
}


'''
return category base on file suffix
    1. loop on the all items in the dictionary
    2. when the suffix is found return category

'''

def pickDirectory(value):
    for ctg, sfx in subdirectories.items():
        for suffix in sfx:
            if suffix == value:
                return ctg
    return 'MISC'
# print(pickDirectory('.pdf'))				


'''
loop thru every items in the directory to get the file type for organizing 
1. use OS library(scandir) 
'''
def organizeDirectory():
    path_dir = input('Please Enter The Desired Path: ').  ### you may put your desire path for Orginizing
    os.chdir(path_dir)
    for item in os.scandir():  ### loop thru every items in the current working directory using the os library
        if item.is_dir():
            continue
        filePath = Path(item)   ### to get the path for every items use the pathlib library
        fileType = filePath.suffix.lower()   ###  return the file extension
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()
