filetype = {
    'video' : ['.mp4', '.mkv', '.3gp', '.avi', '.vob', '.m2ts', '.mov', '.mpg4'], 
    'music' : ['.mp3'],
    'image' : ['.jpg', '.png', '.xcf', '.jpeg'],
    'docs' : ['.pdf', '.txt'],
    'compress' : ['.gz', '.xz', '.bz', '.zip', '.rar'],
    'disk_usb' : ['.img', '.iso'],
    'programs' : ['.exe', '.AppImage', '.deb', '.rpm'],
    'torrent' : ['.torrent']
}

import os
import shutil

path = '/home/arnab/Downloads'
files = os.listdir(path)

for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['video']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Video')):
                shutil.move(os.path.join(path, file), os.path.join(path, 'Video'))
            else:
                os.mkdir(os.path.join(path, 'Video'))
                shutil.move(os.path.join(path, file), os.path.join(path, 'Video'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['music']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Music')):
                shutil.move(os.path.join(path, file), os.path.join(path, 'Music'))
            else:
                os.mkdir(os.path.join(path, 'Music'))
                shutil.move(os.path.join(path, file), os.path.join(path, 'Music'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['image']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Images')):
                shutil.move(os.path.join(path, file), os.path.join(path, 'Images'))
            else:
                os.mkdir(os.path.join(path, 'Images'))
                shutil.move(os.path.join(path, file), os.path.join(path, 'Images'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['docs']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Documents')):
                shutil.move(os.path.join(path, file), os.path.join(path, 'Documents'))
            else:
                os.mkdir(os.path.join(path, 'Documents'))
                shutil.move(os.path.join(path, file), os.path.join(path, 'Documents'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['compress']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Compressed')):
                shutil.move(os.path.join(path, file), os.path.join(path, 'Compressed'))
            else:
                os.mkdir(os.path.join(path, 'Compressed'))
                shutil.move(os.path.join(path, file), os.path.join(path, 'Compressed'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['disk_usb']:
        if i == ext:
            if os.path.isdir(os.path.join(path, "Disk Images")):
                shutil.move(os.path.join(path, file), os.path.join(path, "'Disk Images'"))
            else:
                os.mkdir(os.path.join(path, "Disk Images"))
                shutil.move(os.path.join(path, file), os.path.join(path, "Disk Images"))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['programs']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Programs')):
                shutil.move(os.path.join(path, file), os.path.join(path, 'Programs'))
            else:
                os.mkdir(os.path.join(path, 'Programs'))
                shutil.move(os.path.join(path, file), os.path.join(path, 'Programs'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['torrent']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Torrents')):
                shutil.move(os.path.join(path, file), os.path.join(path, 'Torrents'))
            else:
                os.mkdir(os.path.join(path, 'Torrents'))
                shutil.move(os.path.join(path, file), os.path.join(path, 'Torrents'))