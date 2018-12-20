import urllib.request
import os


def download(url, name):
    if not os.path.exists('Music'):
        os.system('mkdir Music')
    path = 'Music/' + name + '.mp3'
    if not os.path.exists(path):
        try:
            urllib.request.urlretrieve(url, path)
        except AttributeError:
            name = str(hash(url))
            path = 'Music/' + name + '.mp3'
            urllib.request.urlretrieve(url, path)
    print('OK')
    return path
