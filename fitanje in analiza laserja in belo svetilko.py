import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))
#Laser measurements fourier
data1 = np.column_stack(np.genfromtxt("laserBartlett_laser2.txt"))  #Laser
data2 = np.column_stack(np.genfromtxt("laserWelch_laser3.txt"))     
data3 = np.column_stack(np.genfromtxt("laserHann_laser4.txt"))     
#data4 = np.column_stack(np.genfromtxt("laser_spe.dat"))
plt.plot(data1[0] * 0.03829657, data1[1], label = 'Bartlett')
plt.plot(data2[0] * 0.03829657, data2[1], label = 'Welch')
plt.plot(data3[0] * 0.03829657 , data3[1], label = 'Hann')
plt.ylabel(r"$|F(k)|$")
plt.xlabel(u"k[$\u03bcm^{-1}$]")
plt.title("Spektrogram laserja")
plt.xlim(40 * 0.03829657, 120 * 0.03829657)
plt.legend()
plt.savefig("spektrogramlaserjaZOOMUMERITEV.png")
plt.show()
plt.clf()

#White light measurements fourier
data1 = np.column_stack(np.genfromtxt("belaBartlett_bela2.txt"))  #White light
data2 = np.column_stack(np.genfromtxt("belaWelch_bela3.txt"))     
data3 = np.column_stack(np.genfromtxt("belaHann_bela4.txt"))
a = 0.71778201
x0 = 1.80910195
sigma = 0.09179715
xdata = data1[0] 
xdata = xdata[43:55] * 0.03829657
ydata = data1[1]
ydata = ydata[43:55] * 0.03829657
#data4 = np.column_stack(np.genfromtxt("laser_spe.dat"))
plt.plot(data1[0] * 0.03829657, data1[1], label = 'Bartlett')
plt.plot(data2[0] * 0.03829657, data2[1], label = 'Welch')
plt.plot(data3[0] * 0.03829657, data3[1], label = 'Hann')
xdata = np.linspace(42,53, 1000)
plt.plot(xdata * 0.03829657 ,gaus(xdata * 0.03829657,a,x0, sigma), label = 'Gauss fit')
plt.ylabel(r"$|F(k)|$")
plt.xlabel(u"k[$\u03bcm^{-1}$]")
plt.title("Spektrogram bele svetilke")
plt.xlim(10 * 0.03829657,110 * 0.03829657)
plt.legend()
plt.savefig("spektrogrambelesvetilkeZOOMfitUMERITEV.png")
plt.show()
# 0.71778201 1.80910195 0.09179715
#[ 0.73132472 47.23100217 -2.38623219] fit za Hann
#[ 0.73132472 47.23100217 -2.38623219] fit za Welch