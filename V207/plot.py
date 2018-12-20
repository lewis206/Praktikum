import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
t1small, t1big = np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([t1small,t1big], [r"$t_\text{klein} /\si{\second}$", r"$t_\text{groß} /\si{\second}$"], label="tab1", caption="Die Falldauer der kleinen Kugel und die Falldauer der großen Kugel.", roundPrecision=1)
tab1.writeFile("build/tab1.tex")

T11, t1 = np.genfromtxt("data/datab.txt", unpack=True)
T1= T11+273.15
tab2 = TexTable([T1,t1], [r"T /\si{\kelvin}", r"t /\si{\second}"], label="tab2", caption="Die Fallzeit in Abhängigkeit zur Temperatur der Flüssigkeit.", roundPrecision=1)
tab2.writeFile("build/tab2.tex")

T21, t2 = np.genfromtxt("data/datac.txt", unpack=True)
T2= T21+273.15
tab3 = TexTable([T2,t2], [r"T/\si{\kelvin}", r"t /\si{\second}"], label="tab3", caption="Die Fallzeit in Abhängigkeit zur Temperatur der Flüssigkeit.", roundPrecision=1)
tab3.writeFile("build/tab3.tex")
#extra values 
#a)
mbig=4.21/1000 #kg
msmall=3.71/1000 #kg
Vbig=(0.0158/2)**3 *(4/3)*np.pi #m^3
Vsmall=(0.0156)**3 * (4/3) *np.pi #m^3

#b)
rhoFl= 0.9982067*1000 # kg/m^3
x = 0.1 #m 
Ksmall= 0.07640*1e-6 

#e)
dbig= 0.0158
dsmall= 0.0156
#functions 

def func(x):
    return x+1

def f(x, a, b, c, d):
     return a * np.sin(b * x + c) + d

def getEta(T, A, B):
    return np.log(A)*(B/T) 
#calculate 
#a)
rhobig= mbig/Vbig 
rhosmall = msmall/Vsmall 
#b)
tsmall=ufloat(t1small.mean(), t1small.std())
tbig= ufloat(t1big.mean(), t1big.std())

#c)
eta= Ksmall* (rhosmall- rhoFl)*tsmall
Kbig=eta/((rhobig-rhoFl)*tbig)

#d) 
eta1=np.abs(Kbig.nominal_value*(rhobig- rhoFl)*t1) 
eta2= np.abs(Kbig.nominal_value*(rhobig- rhoFl)*t2) 

#g) 
vwater1= x/tsmall
vwater2= x/tbig
#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
params1, pcov1 = curve_fit(getEta, T1, np.log(eta1))
params2, pcov2 = curve_fit(getEta, T2, np.log(eta2))

newT1= np.linspace(T1[0], T1[-1], 200)
newT2= np.linspace(T2[0], T2[-1], 200)

#e)
rey1= rhoFl*dsmall*vwater1/eta 
rey1= rhoFl*dbig*vwater2/eta 


#save solution 

file = open("build/solution.txt", "w")
file.write("Dichte_klein= {}\nDichte_groß= {}\nDichte_Fl= {}\nA1= {}\nB1= {}\nA2= {}\nB2= {}\nReynoldsche Zahl= {}".format(rhosmall, rhobig, rhoFl, params1[0], params1[1], params2[0], params2[1], rey1))
file.close()

#Make plots for data
plt.figure(1)
plt.plot(1/T1, np.log(eta1), "xr", label="Daten")
plt.plot(1/newT1, function(newT1, *params1), "r--", label="Fit", linewidth=1.0)
plt.xlabel(r"$\frac{1}{T}/\si[per-mode=fraction]{\per\kelvin}$")
plt.ylabel(r"$log(\eta)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

plt.figure(2)
plt.plot(1/T2, np.log(eta2), "xr", label="Daten")
plt.plot(1/newT2, function(newT2, *params2), "r--", label="Fit", linewidth=1.0)
plt.xlabel(r"$\frac{1}{T}/\si[per-mode=fraction]{\per\kelvin}$")
plt.ylabel(r"$log(\eta)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot2.pdf")

#curvefit plot

#plt.errorbar(x, y, yerr=err_y, fmt='rx', label='Daten')
#t = np.linspace(-0.5, 2 * np.pi + 0.5)
#plt.plot(t, f(t, *parameters), 'b-', label='Fit')
#plt.plot(t, np.sin(t), 'g--', label='Original')
#plt.xlim(t[0], t[-1])
#plt.xlabel(r'$t$')
#plt.ylabel(r'$f(t)$')
#plt.legend(loc='best')
#plt.tight_layout()
#plt.savefig("build/plot1b.pdf")

