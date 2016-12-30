#coding:utf8
'''
Created on 2016年12月30日

@author: Zephyr
'''
import urllib2
from pip._vendor.requests.api import request
import cookielib


url ="http://www.baidu.com"

print "first method"

response1 = urllib2.urlopen(url)

print response1.getcode()

print len(response1.read())

print "method2"


print ""
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response2 = urllib2.urlopen(url)
print response2.getcode()
print response2.read()
print cj
