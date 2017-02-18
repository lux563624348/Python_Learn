########################################################################
#### Yes or No
###### Xiang Li Feb.18.2017
########################################################################
########################################################################

##Module

########################################################################

def y_n():
	while True:
		ok = input('Please type your response. (yes or no)\n')
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		else:
			print('Not a valid answer, try again.')
