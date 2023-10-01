import urllib
import urllib.request

url = 'http://www.google.com'
try:
    site = urllib.request.urlopen(url)
except:
    print(f'O site {url} não está acessível!')
else:
    print(f'O site {url}, foi acessado com sucesso')