#coding=UTF_8
##函数与文件操作例程
#


from sys import argv

script , input_file=argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_one_line(line,f):
	for line in range(1,line):	
		f.readline()
	line = line + 1
	print line,f.readline()



print "Now,we will print the whole file:"
txt = open(input_file)
print_all(txt)

print "Now,we will print one line."
current_line = input("which line do you want print? ")
rewind(txt)
print_one_line(current_line,txt)

txt.close()

