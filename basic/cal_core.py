########################################################################
#### Calculation of main function
###### Xiang Li Feb.18.2017
########################################################################
########################################################################

##Module

########################################################################

ratio_k_m = 1
t_stepsize = 0.1

def cal_main(t_end):
	stepnumber = int( t_end/t_stepsize)
	#print(stepnumber)
	t = [0]
	v = [-1]
	x = [1]

	for i in range(1, stepnumber, 1):
		t.append(i*t_stepsize)
		x.append(x[i-1]+ v[i-1]*t_stepsize)
		v.append(v[i-1]-x[i]*t_stepsize)
		
	return x,v,t
