import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#Laser measurements fourier
data1 = np.column_stack(np.genfromtxt("laserBartlett_laser2.txt"))  #Laser
data2 = np.column_stack(np.genfromtxt("laserWelch_laser3.txt"))     
data3 = np.column_stack(np.genfromtxt("laserHann_laser4.txt"))     
#data4 = np.column_stack(np.genfromtxt("laser_spe.dat"))
plt.plot(data1[0] * 0.03829657, data1[1], label = 'Bartlett')
plt.plot(data2[0] * 0.03829657, data2[1], label = 'Welch')
plt.plot(data3[0] * 0.03829657, data3[1], label = 'Hann')
plt.ylabel(r"$|F(k)|$")
plt.xlabel(u"k[$\u03bcm^{-1}$]")
plt.legend()
plt.title("Spektrogram laserja")
plt.savefig("spektrogramlaserjaUMERITEV.png")
plt.show()
plt.clf()

#White light measurements fourier
data1 = np.column_stack(np.genfromtxt("belaBartlett_bela2.txt"))  #White light
data2 = np.column_stack(np.genfromtxt("belaWelch_bela3.txt"))     
data3 = np.column_stack(np.genfromtxt("belaHann_bela4.txt"))      
#data4 = np.column_stack(np.genfromtxt("laser_spe.dat"))
plt.plot(data1[0] * 0.03829657, data1[1], label = 'Bartlett')
plt.plot(data2[0] * 0.03829657, data2[1], label = 'Welch')
plt.plot(data3[0] * 0.03829657, data3[1], label = 'Hann')
plt.ylabel(r"$|F(k)|$")
plt.xlabel(u"k[$\u03bcm^{-1}$]")
plt.legend()
plt.title("Spektrogram bele svetilke")
plt.savefig("spektrogrambelesvetilkeUMERITEV.png")
plt.show()

#Hg light measurements fourier
data1 = np.column_stack(np.genfromtxt("hgBartlett_hg2.txt"))  #Hg svetilka
data2 = np.column_stack(np.genfromtxt("hgWelch_hg3.txt"))    
data3 = np.column_stack(np.genfromtxt("hgHann_hg4.txt"))     
data4 = np.column_stack(np.genfromtxt("hg1.txt"))
plt.plot(data1[0] * 0.03829657, data1[1], label = 'Bartlett')
plt.plot(data2[0] * 0.03829657, data2[1], label = 'Welch')
plt.plot(data3[0] * 0.03829657, data3[1], label = 'Hann')
#plt.plot(data4[0], data4[1])
plt.ylabel(r"$|F(k)|$")
plt.xlabel(u"k[$\u03bcm^{-1}$]")
plt.legend()
plt.title("Spektrogram Hg svetilke")
plt.savefig("spektrogramhgsvetilkeUMERITEV.png")
plt.show()
plt.clf()

figure, axis = plt.subplots(4, 1)
figure.suptitle("Spektrogram Hg svetilke z okenske funkcije Bartlett, Welch, Hann in brez")
axis[0].plot(data1[0], data1[1])
axis[1].plot(data2[0], data2[1])
axis[2].plot(data3[0], data3[1])
axis[3].plot(data4[0], data4[1])
figure.tight_layout()
plt.savefig("Spektrogramefunkcijeprimerjava.png")
#plt.show()
