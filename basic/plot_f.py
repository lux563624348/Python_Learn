########################################################################
#### Make plot
###### Xiang Li Feb.18.2017
########################################################################
########################################################################

##Module
import matplotlib.pyplot as plt

########################################################################



#### Decoration
def plot_2d (t,x):	
	x_min = -3
	x_max = 3
	t_min = 0
	t_max = 15
	#t_axis = linspace(t_max, t_min, 20)
	#lines = plt.plot(t,x)

	#plt.raw_input('Press the Return key to quit:')
	plt.xlabel('Time')
	plt.ylabel('Distance from origin position')
	plt.title('Harmonic Oscillator')
	plt.plot(t,x)
	plt.show()
	print('Done?')
	#Generate the pictures
	#counter = 0
	#for i in range(1,stepnumber,1):
	#	plt.axis([t_min, t_max, x_min, x_max])
	#	plt.plot(t[i],x[i],'bo')
	#	plt.savefig('tmp_%04d.png' % counter)
	#	counter += 1

	#cmd = 'convert -delay 50 tmp_*.png movie.gif'
	#plt.plot(t,x,'bo')
	#plt.show()
