import random, math, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def show_conf(L, sigma, title, fname):
    plt.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = plt.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                plt.gca().add_patch(cir)
    plt.axis('scaled')
    plt.title(title)
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.savefig(fname)
    plt.show()
    plt.close()

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

N = 64
eta = 0.72
filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    N_sqrt = int(math.sqrt(N) + 0.5)
    delxy = 1.0/ (2.0 * N_sqrt)
    two_delxy = 2.0 * delxy
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
    print 'starting from a new square-lattice configuration'

sigma = math.sqrt(eta / (N * math.pi))
delta = sigma * 0.3
n_steps = 10000
for step in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta) , a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b, c) for c in L if c != a)
    if min_dist > 2.0 * sigma:
        a[:] = [b[0] % 1.0, b[1] % 1.0]

f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
show_conf(L, sigma, 'N='+str(N)+' $\eta =$'+str(eta), 'configuration_'+str(N)+'_'+str(eta)+ '.png')
