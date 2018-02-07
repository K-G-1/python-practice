#coding=UTF-8
##变量的使用方法，包括数字与字符串

print "start! "
print "________only num ____________"

cars = 100
space_in_car = 4.0
drives = 10
passengers = 90
cars_no_drives = cars - drives
cars_drives = drives
carpool_capacity = cars_drives * space_in_car
average_passengers_per_car = passengers / cars_drives

print "There are ",cars,"cars available."
print "There are only ",drives,"drives available."
print "There will be ",cars_no_drives,"empty cars today."
print "we can transport ",carpool_capacity,"people today."
print "We have ",passengers,"to carpool today."
print "We need to put about ",average_passengers_per_car,"in each car ."


print "__________there are some string___________"

name = "K.G."
age = "22"
height = 176 	# 我不算矮吧
weight =  85	#我真的不重
eyes_colour = "brown"
hair_colour = "black"

# 注意format 的使用
print "My name is %s ,%s age."%(name,age)
print "I have %d inches tall."%height
print "I am %d pounds heavy."%weight 
print "I have %s eye and %s hair" %(eyes_colour,hair_colour)


print "____________format()___________"
my_str1 = "hello"
my_str2 = "world"

#注意 ‘.’ 不是 ‘，’
print "{0} {1} {1} {0}".format('Hello','world')
print "{0} {1}".format(my_str1,my_str2)

print "I love {KG}".format(KG='you')

#对齐设置 
#>	右对齐 
#<	(默认)左对齐 
#=	在小数点后对其 
#^ 	中间对其

pi = 3.1415926
print format("string","2s")

print format(pi,".5f")
print "{0:>15}".format(pi)
print "{0:15.4f}".format(pi)
print "{0:>15.4f}".format(pi)
print "{0:<15.4f},{1}".format(pi,"string")