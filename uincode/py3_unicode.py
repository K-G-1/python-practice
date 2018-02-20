# -*- coding:utf-8 -*-
# 
import json

dict_list = {"topic": "\u5168\u96c6", "url": "www.acglala.com//dhxf/DARLING0in0the0FRANKXX/down/1-1.html"}

print ('%r'%dict_list['topic'])

filename = open('example.txt', 'w',encoding = 'utf-8')
string = str(dict_list)
filename.write(string)
filename.close()