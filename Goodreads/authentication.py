import os
import time
from rauth.service import OAuth1Service, OAuth1Session
import xml.etree.ElementTree as ET
#from lib import webbroswer as webbroswer
#import oauth2 as oauth
#import urlparse

url = 'http://www.goodreads.com'
request_token_url = '%s/oauth/request_token/' % url
authorize_url = '%s/oauth/authorize/' % url
access_token_url = '%s/oauth/access_token/' % url

goodreads = OAuth1Service(
consumer_key='',
consumer_secret='',
name='goodreads',
request_token_url='https://www.goodreads.com/oauth/request_token',
authorize_url='http://www.goodreads.com/oauth/authorize',
access_token_url='https://www.goodreads.com/oauth/access_token',
base_url='http://www.goodreads.com/'
)

# head_auth=True is important here; this doesn't work with oauth2 for some reason
request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

authorize_url = goodreads.get_authorize_url(request_token)
os.startfile(authorize_url)

#webbrowser.open(authorize_url, new=0, autoraise=True)
print ('Visit this URL in your browser: ' + authorize_url)
accepted = 'n'
while accepted.lower() == 'n':
# you need to access the authorize_link via a browser,
# and proceed to manually authorize the consumer
    accepted = input('Have you authorized me? (y/n) ')


session = goodreads.get_auth_session(request_token, request_token_secret)
useridxml = session.get('https://www.goodreads.com/api/auth_user')
root = ET.fromstring(useridxml.content)

for child in root:
    if str(child.tag)=='user':
        userid = (child.attrib['id'])
        break

sessionparams = {'id':userid}
#print(type(session))
userfriendsxml = session.get('https://www.goodreads.com/friend/user.xml',params={'id':userid})
root = ET.fromstring(userfriendsxml.content)

print('reached here')

nodelist = root.findall('./friends/user/id')
print("Listing owned books by your friends on goodreads")

for each in nodelist:
    print(each.text)
    ownedbooksxml = session.get('https://www.goodreads.com/owned_books/user.xml', params={'id':each.text})
    ownedbooks = ET.fromstring(ownedbooksxml.content)

    xmlout = ET.tostring(ownedbooks)
    myfile = open(each.text+".xml", "wb")
    myfile.write(xmlout)
    # print(ownedbooksxml.content)

    # break


#for node in root:
# if(str(node.tag)=='friends'):
# for child in node:
# if(str(child.tag)=="user"):
# for grandchild in child:
# print(grandchild.text)
xmlout = ET.tostring(root)
myfile = open("xmloutput.xml", "wb")
myfile.write(xmlout)

# f = open('xmloutput.xml', 'w')
# f.write(str(userfriendsxml.content))



# book_id 631932 is "The Greedy Python"
#data = {'id': 'to-read', 'book_id': 631932}

# add this to our "to-read" shelf
#response = session.post('http://www.goodreads.com/shelf/add_to...', data)

# these values are what you need to save for subsequent access.
#ACCESS_TOKEN = session.access_token
#ACCESS_TOKEN_SECRET = session.access_token_secret 