#coding=UTF_8
##rw file example
#
#close 		关闭文件
#read 		读取文件
#readline 	读取某一行
#truncate 	清空文件
#write 		写数据



from sys import argv

script ,file_name = argv

print "We will erase %r:"%file_name
print "Do you want do that?"
raw_input('?')

file = open(file_name,"w")
file.encoding = 'utf-8'
file.truncate()

print "Now,we will write something."
line1 = raw_input("what will be write in line1? ")
line2 = raw_input("what will be write in line2? ")
line3 = raw_input("what will be write in line3? ")

file.write(line1)
file.write('\n')

file.write(line2)
file.write('\n')

file.write(line3)
file.write('\n')


file.close()


	
