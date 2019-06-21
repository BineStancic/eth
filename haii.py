from scipy import stats  
import numpy as np  
import matplotlib.pylab as plt
from scipy import optimize

#All times are in us
tau = 2.2
#print tau
#define the function for the probability density function
def muon(t):
    return (1/tau)*np.exp(-t/tau)


#define the function for the decay of the particle that is not tau
notau = 1
def notmuon(t):
    return (1/notau)*np.exp(-t/notau)

#Define the background function
def background(t):
    x = np.random.uniform()
    if (x<=0.8):                  #80% of the time the muon is detected
        return muon(t)
    if (x>0.8):                  #20% of the time the other particle is detected
        return(notmuon(t))

#Time acceptance function
G = 1
def a(t):
    return(1-np.exp(-t/G))

#Modified function with time acceptance
def acceptance(t):
    return(background(t)*a(t))

#ymax = optimize.fmin(-(acceptance(t)),1)*1.05
#print ymax
ymax = (0.01+(1/notau))
times = []             #Empty array for set of 500 average decay times
decayt = []            #Empty array for set of 1000 decays

j=0
while j < 50:
    decayt = []
    i = 0
    n = 1000
    while i < n:
        t = np.random.uniform(0,50)
        y1 = acceptance(t)
        y2 = np.random.uniform()*ymax
        #print i,y1
        if (y2<y1):
            decayt.append(t)
            i = i + 1
            #print i,j
        else:
            i = i
#The first interval plot the histogram of the probability density function
    if j == 1:
        plt.hist(decayt[:], bins = 50)
        plt.xlabel("time(us)")
        plt.ylabel('Probability of decay')
        plt.show()

    #Find the average of 1000 decay times after every interval and append to array
    tau_av = np.mean(decayt)
    times.append(tau_av)
    j = j + 1

#printing the mean and standard deviations of the decay times
m = np.mean(times)
print('mean:'+str(m))
std = np.std(times)
print('standard deviation: '+str(std))


#Writing the average decay times to a .txt file
with open('times.txt', 'w') as f:
    for item in times:
        f.write("%s\n" % item)
'''
haii = []
t=0
while t<4:
    haii.append(background(t))
    t=t+0.01

plt.plot(haii)
plt.show()
'''

#Plot a histogram of 500 average decay times
plt.hist(times[:], bins = 25)
plt.axvline(x=tau, color='r', label='Actual decay time')
plt.xlabel('Decay time(us)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
