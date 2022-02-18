# import socket
# import urllib.request
"""
设置时间超时,抛出错误

"""
# response = urllib.request.urlopen('http://www.httpbin.org/get',timeout=0.1)
# print(response.read())

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://www.httpbin.org/get',timeout=0.1)
    print(response)
    
except urllib.error.URLError as e:
    if isinstance(e.errno,socket.timeout):
        print("Time Out") 
    