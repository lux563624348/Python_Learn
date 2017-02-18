########################################################################
####
###### Xiang Li Feb.18.2017
########################################################################
########################################################################

##Module

########################################################################
def time_end_set():

	for i in range(1,5) :
		t = int(input("Please enter the end time: "))
		if t < 0:
			print('Wrong value, end time must be positive!')
			continue
		elif t == 0:
			print('Zero, not valid')
			continue
		else:
			print("The end time is ", t)
			return t
			break
