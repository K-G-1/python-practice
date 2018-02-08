#coding=UTF_8
##read file example

from sys import argv

script,txt_name= argv

txt = open(txt_name)

print "this  is your %r:"%txt_name;

print txt.read()

txt.close()
