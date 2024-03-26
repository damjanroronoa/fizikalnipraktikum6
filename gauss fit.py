

import numpy as np 
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt
data1 = np.column_stack(np.genfromtxt("belaHann_bela4.txt"))  #White light
xdata = data1[0]
xdata = xdata[43:55] * 0.03829657 * 2
ydata = data1[1]
ydata = ydata[43:55]

x = xdata
y = ydata

n = len(x)                          #the number of data
mean = sum(x*y)/n                   #note this correction
sigma = sum(y*(x-mean)**2)/n        #note this correction

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt,pcov = curve_fit(gaus,x,y,p0=[1,mean,sigma])
print(popt)
plt.plot(x * 0.03829657 * 2,y,'b+:',label='data')
plt.plot(x * 0.03829657 * 2,gaus(x,*popt),'ro:',label='fit')
plt.legend()
plt.title('Fig. 3 - Fit for Time Constant')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()