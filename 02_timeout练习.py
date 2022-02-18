from socket import timeout
import urllib.request
response = urllib.request.urlopen('http://www.httpbin.org/get',timeout=0.1)
print(response.read())