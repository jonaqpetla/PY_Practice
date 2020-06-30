# we're working at transport layer here, assuming a connection can be made
# socket to socket
# port 80 assumed for http, 443 for https

# sockets ==============================================================================================

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )     # trying to establish a connection, might fail
                                            # function with input of a tuple
# once a socket is connected, decide what application protocol you want
# look at telnet utility on linux systems to get web pages manually. same shit
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP:/1.0\n\n'.encode()
                                            # encode() converts from unocode to utf-8
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()

# in most cases we'll need to process the incoming text streams
# ascii hack - ord('\n') returns 10 - ascii code for '\n'

# urllib, html parsing, beautiful soup =================================================================

# to avoid manually opening sockets, use urllib, for http work
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
# the returned object can be handled like a file stream

# use beautiful soup to parse html - no need to reinvent the wheel
from bs4 import BeautifulSoup
html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))    # find a link in the page

# there might be ssl ceritificate errors in this workflow when encountering https://
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# html = urllib.request.urlopen(url, context=ctx).read()

# XML & JSON ===========================================================================================