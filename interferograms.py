import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#First we plot the interferograms, or our measurements that we fourier transform later
#

data = np.column_stack(np.genfromtxt("laser1.dat"))  #open the file
#print(data)                                         #quick check
plt.plot((data[0] - 512) / 19.7344331, data[1])                     #plotting the measurements with -512, so that we get the 0 in the center
plt.xlabel(u"x[\u03bcm]")                                  #just like our measurements
plt.ylabel(r"$f(x)$")                          
plt.title("Interferogram laser")
plt.savefig("interferogramlaserUMERITEV.png")
plt.show()                                           #Laser looks like a sine wave, just as expected
plt.clf()

data1 = np.column_stack(np.genfromtxt("hg2.dat"))    
#print(data1)                                        
plt.plot(data1[0] - 512, data1[1])                   
plt.xlabel("Korak")
plt.ylabel(r"$f(x)$")
plt.title("Interferogram Hg svetilka")
plt.savefig("interferogramhg.png")
#plt.show()                                           #Hg light
plt.clf()

data2 = np.column_stack(np.genfromtxt("bela1.dat"))
#print(data2)                                        
plt.plot(data2[0] - 512, data2[1])                   
plt.xlabel("Korak")
plt.ylabel(r"$f(x)$")
plt.title("Interferogram Bela svetilka")
plt.savefig("interferogrambela.png")
#plt.show()                                           # the white light looks like a wave packet
plt.clf()

#INTERFEROGRAMS TOGETHER WITH LABELS AND TITLE
figure, axis = plt.subplots(3, 1)
figure.tight_layout()
plt.xlabel("Korak")
axis[0].set_ylabel(r"$f(x)$")                       #maybe better to have only one f(x)? no idea
axis[1].set_ylabel(r"$f(x)$")                       #maybe better to have only one f(x)? no idea
axis[2].set_ylabel(r"$f(x)$")                       #maybe better to have only one f(x)? no idea
axis[0].plot(data[0] - 512, data[1])
axis[0].set_title("Laser, Hg svetilka, Bela svetilka")
axis[1].plot(data1[0] - 512, data1[1])
#axis[1].set_title("Hg svetilka")
axis[2].plot(data2[0] - 512, data2[1]) 
#axis[2].set_title("Bela svetilka")
plt.savefig("interferogramizaedno.png")
#plt.show()

#INTERFEROGRAMS TOGETHER WITHOUT LABELS AND WITHOUT TITLES
figure, axis = plt.subplots(3, 1)
figure.tight_layout()
axis[0].plot(data[0] - 512, data[1])
axis[1].plot(data1[0] - 512, data1[1])
#axis[1].set_title("Hg svetilka")
axis[2].plot(data2[0] - 512, data2[1]) 
#axis[2].set_title("Bela svetilka")
plt.savefig("interferogramizaednobez.png")
#plt.show()