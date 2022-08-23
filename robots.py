import urllib.request
import io


def get_robot(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    path = path + "robots.txt"
    req = urllib.request.urlopen(path, data=None)
    data = io.TextIOWrapper(req)
    return data.read()


print(get_robot('www.google.com'))
