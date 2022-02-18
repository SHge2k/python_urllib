# import urllib.request
# response = urllib.request.urlopen("http://www.python.org")
# #print(response.read().decode('utf-8'))
# print(type(response))

# from urllib import response
# import urllib.request 
# response= urllib.request.urlopen("http://www.python.org")
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'name':'gerem'}),encoding='utf-8')
response = urllib.request.urlopen('http://www.httpbin.org/post',data=data)
print(response.read().decode('utf-8'))