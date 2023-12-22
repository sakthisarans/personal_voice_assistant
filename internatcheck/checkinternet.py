import urllib.request

def check_internet(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False