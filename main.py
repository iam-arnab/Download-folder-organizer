#!/usr/bin/python3
import shutil
import os
filetype = {
    'video': ['.mp4', '.mkv', '.3gp', '.avi', '.vob', '.m2ts', '.mov', '.mpg4'],
    'music': ['.mp3', '.3ga', '.aifc', '.m3u', '.m3u8', '.m4p', '.m4r'],
    'image': ['.jpg', '.png', '.xcf', '.jpeg', '.gif', '.tif', '.webp'],
    'docs': ['.json', '.pdf', '.txt', '.doc', '.html', '.htm', '.xls', '.xlsx', '.ppt', '.pptx', '.docx', '.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.xml', '.epub'],
    'compress': ['.gz', '.xz', '.bz', '.zip', '.rar', '.7z', '.arj'],
    'disk': ['.img', '.iso', '.toast', '.vcd'],
    'programs': ['.exe', '.AppImage', '.deb', '.rpm', '.dmg', '.bin', '.jar', '.py'],
    'torrent': ['.torrent'],
    'fonts': ['.otf', '.tff']
}


path = '/home/arnab/Downloads'
files = os.listdir(path)

for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['video']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Video')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Video'))
            else:
                os.mkdir(os.path.join(path, 'Video'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Video'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['music']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Music')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Music'))
            else:
                os.mkdir(os.path.join(path, 'Music'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Music'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['image']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Images')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Images'))
            else:
                os.mkdir(os.path.join(path, 'Images'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Images'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['docs']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Documents')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Documents'))
            else:
                os.mkdir(os.path.join(path, 'Documents'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Documents'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['compress']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Compressed')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Compressed'))
            else:
                os.mkdir(os.path.join(path, 'Compressed'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Compressed'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['disk']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Disk Images')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, "'Disk Images'"))
            else:
                os.mkdir(os.path.join(path, "Disk Images"))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, "Disk Images"))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['programs']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Programs')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Programs'))
            else:
                os.mkdir(os.path.join(path, 'Programs'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Programs'))
for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['torrent']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Torrents')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Torrents'))
            else:
                os.mkdir(os.path.join(path, 'Torrents'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Torrents'))

for file in files:
    temp = file.split('.')
    ext = '.' + temp[-1]
    for i in filetype['fonts']:
        if i == ext:
            if os.path.isdir(os.path.join(path, 'Fonts')):
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Fonts'))
            else:
                os.mkdir(os.path.join(path, 'Fonts'))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, 'Fonts'))
