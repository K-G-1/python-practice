#coding=UTF_8
## 使用字典
#

cities  = {'CA':'San Francisco','Mi':'Detrot','FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
	if state in themap:
		return themap[state]
	else:
		return 'Not found'

#
cities['_find'] = find_city

while True:
	print "states?(Enter to quit)"
	state = raw_input('>')

	if not state:
		break

	#this line is the most important ever!study!
	city_found = cities['_find'](cities,state)
	#city_found = find_city(cities,state)   #this line is also ok
	

	print city_found