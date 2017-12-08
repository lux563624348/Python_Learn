########################################################################
#### MAIN  
###### Xiang Li Feb.18.2017
########################################################################
########################################################################

##Module

#from matplotlib.pyplot import *
import ask_ok as ask_ok
import Set_up as sup
import OI as oi
import cal_core as cal
import plot_f as plot_f
import numpy as np
########################################################################


print('Start !')
print('Try the first parameter?\n')
reply = ask_ok.y_n()




# Make file and main loop.
while reply:

	t_end = sup.time_end_set()

	x,v,t = cal.cal_main( t_end)

	oi.f_write('data_out.dat', t,x)

	plot_f.plot_2d(t,x)

	print('Try a different parameter?\n')
	reply = ask_ok.y_n()




