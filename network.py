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

# XML and JSON
# XML ==================================================================================================
# ^ built for data sharing among application processes. Uses wire protocol (really? serialize - deserialize)

# XML: start tag, end tag, attributes, text content. Seft closing tags in the absence of text content
# e.g. <person height=170>Jonaq</person>. May contain tags content - think of it like a tree
# XML can have only one outer tag. Document specs are exempt from this rule, 
# but they have to be at the very beginning, and not after a \n for example

import xml.etree.ElementTree as ET 

input = '''<?xml version="1.0" encoding="utf-8" ?>
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

tree = ET.fromstring(input)

# getting the first matches
print('Name:', tree.find('users/user/name').text)       # getting content
print('Attr:', tree.find('users/user').get('x'))        # getting attributes

# getting everything
lst = tree.findall('users/user')
print('\nUser count: ', len(lst))

for item in lst:
    print('Name: ', item.find('name').text)
    print('id: ', item.find('id').text)
    print('Attribute: ', item.get('x'))

print()

# XML schema Validation can be done using pyxsd
# xsd is the most commonly used language for xml schema specification
# a valid schema of our example xml would be:
sch = '''<?xml version="1.0" encoding="utf-8" ?>
<xs:complexType name='stuff'>
    <xs:complexType name='users'>
        <xs:sequence>
        <xs:complexType name='user' minOccurs='1' maxOccurs='10'>
            <xs:sequence>
            <xs:element name='id' type='xs:integer'/>
            <xs:element name='id' type='xs:string'/>
            </xs:sequence>
        </xs:complexType>
        </xs:sequence> 
    </xs:complexType>
</xs:complexType>
'''

# JSON - Javascript Object Notation ====================================================================
# json is better for just pulling data out of a system. not as cumbersome as xml's hierarchical structure
# json is not internationally standardized, it's just that people like it and use it
# "key" : "value" pairs, can have objects as value

import json
data = '''
{
    "name" : "Chuck",
    "phone" : 
    {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : 
    {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)                 # load from string, returns a dictionary
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])

# json might have a list of multiple dictionaries, then info will also be a list of dictionaries
# json may not be able to represent data as complex as xml, but dealing with lists and dicts are simpler

# WEB Services =========================================================================================