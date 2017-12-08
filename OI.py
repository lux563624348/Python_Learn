########################################################################
#### Reading and Writing Files
###### Xiang Li Feb.18.2017
########################################################################
########################################################################

##Module

########################################################################


# f = open(filename, mode)
def f_read (filename):
	f = open (filename, 'r')
	read_data = float( f.read())
	f.close()
	#print (read_data)
	return read_data

#Mode: 'r' only be read,	 't' text mode
#      'w' for only writing  '+' a disk file for updating (Reading and writing)	 
#      'a' for appending     'U' universal newlines mode ???
#      'r+'reading and writing.
#	   'b' binary mode        For example, 'w+b'


# 2D data, t-x
def f_write (filename,t,x):
	#print(len(t))
	f = open (filename, 'w')
	for i in range (len(t)):
		f.write('%10.5f' % (t[i]))
		f.write('%10.5f' % (x[i]))
	f.close()
	

