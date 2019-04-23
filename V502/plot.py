import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit
from something import some 
#Generate data 
# V501 Messung 
index1, Ud1= some.neueWerte(file_name="data/dataa1.txt", finished_file="build/taba1.tex",  vars_name=[r"Index", r"$U_\text{d} / \si{\volt}$"], label_text="taba1", caption_text=r"Die Indexwerte entsprechen der Höhe, die bei der jeweiligen Ablenkspannung $U_\text{d}$ und der Beschleunigungsspannung $U_\text{B} = \SI{180}{\volt}$ gemessen wurden. Der Indexwert $1$ entspricht einer Höhe von $\SI{0.6}{\centi\meter}$." , precision=1)
index2, Ud2= some.neueWerte(file_name="data/dataa2.txt", finished_file="build/taba2.tex",  vars_name=[r"Index", r"$U_\text{d} / \si{\volt}$"], label_text="taba2", caption_text=r"Die Indexwerte entsprechen der Höhe, die bei der jeweiligen Ablenkspannung $U_\text{d}$ und der Beschleunigungsspannung $U_\text{B} = \SI{230}{\volt}$ gemessen wurden. Der Indexwert $1$ entspricht einer Höhe von $\SI{0.6}{\centi\meter}$." , precision=1)
index3, Ud3= some.neueWerte(file_name="data/dataa3.txt", finished_file="build/taba3.tex",  vars_name=[r"Index", r"$U_\text{d} / \si{\volt}$"], label_text="taba3", caption_text=r"Die Indexwerte entsprechen der Höhe, die bei der jeweiligen Ablenkspannung $U_\text{d}$ und der Beschleunigungsspannung $U_\text{B} = \SI{280}{\volt}$ gemessen wurden. Der Indexwert $1$ entspricht einer Höhe von $\SI{0.6}{\centi\meter}$." , precision=1)
index4, Ud4= some.neueWerte(file_name="data/dataa4.txt", finished_file="build/taba4.tex",  vars_name=[r"Index", r"$U_\text{d} / \si{\volt}$"], label_text="taba4", caption_text=r"Die Indexwerte entsprechen der Höhe, die bei der jeweiligen Ablenkspannung $U_\text{d}$ und der Beschleunigungsspannung $U_\text{B} = \SI{330}{\volt}$ gemessen wurden. Der Indexwert $1$ entspricht einer Höhe von $\SI{0.6}{\centi\meter}$." , precision=1)
index5, Ud5= some.neueWerte(file_name="data/dataa5.txt", finished_file="build/taba5.tex",  vars_name=[r"Index", r"$U_\text{d} / \si{\volt}$"], label_text="taba5", caption_text=r"Die Indexwerte entsprechen der Höhe, die bei der jeweiligen Ablenkspannung $U_\text{d}$ und der Beschleunigungsspannung $U_\text{B} = \SI{380}{\volt}$ gemessen wurden. Der Indexwert $1$ entspricht einer Höhe von $\SI{0.6}{\centi\meter}$." , precision=1)
d= index1*0.6 -0.6 # Unterer Abstand bis oben in centimeter 
dnew = d/100 #dnew in Metern
# V501 Frequenzen
index12, frequenz1 = some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"Index", r"$\nu_\text{Sä} / \si{\hertz}$"], label_text="tabb", caption_text=r"Die Frequenzen der Sägezahnspannung.", precision=2)
#V502 Messung
index6, I1= some.neueWerte(file_name="data/datac1.txt", finished_file="build/tabc1.tex",  vars_name=[r"Index", r"$I / \si{\ampere}$"], label_text="tabc1", caption_text=r"Die Indexwerte entsprechen der Höhe bei dem jeweiligen Strom und der Beschleunigungsspannung $U_\text{B} = \SI{250}{\volt}$." , precision=2)
index7, I2= some.neueWerte(file_name="data/datac2.txt", finished_file="build/tabc2.tex",  vars_name=[r"Index", r"$I / \si{\ampere}$"], label_text="tabc2", caption_text=r"Die Indexwerte entsprechen der Höhe bei dem jeweiligen Strom und der Beschleunigungsspannung $U_\text{B} = \SI{360}{\volt}$." , precision=2)
#V502 Erdmagnetfeld 
I_hor = 0.19 #Ampere
phi = 79.5 #Grad
N = 20 #Windungen 
R = 0.282 #Meter
B1 = 4*np.pi*1e-7 * (8/np.sqrt(125)) * (N/R) * I1  * (1/np.sqrt(8*250))
B2 = 4*np.pi*1e-7 * (8/np.sqrt(125)) * (N/R) * I2 * (1/np.sqrt(8*360))
L= 0.143
s = dnew
DundL= s/(L**2 +s**2) 
B1 = np.delete(B1, (-1), 0)
B2 = np.delete(B2, (-1), 0)
DundL = np.delete(DundL, (-1), 0)
#Generate table with calculated data
some.tabelle([Ud1/180, Ud2/230, Ud3/280, Ud4/320, Ud5/380, d], finished_file="build/tab1.tex", vars_name=[r"$\frac{U_\text{d, 1}}{U_\text{B, 1}}$",r"$\frac{U_\text{d, 2}}{U_\text{B, 2}}$",r"$\frac{U_\text{d, 3}}{U_\text{B, 3}}$",r"$\frac{U_\text{d, 4}}{U_\text{B, 4}}$",r"$\frac{U_\text{d, 5}}{U_\text{B, 5}}$", r"$D / \si{\meter}$"], label_text="tab1", caption_text=r"Das Verhältnis der Ablenkspannung und der Beschleunigungsspannung aufgetragen gegen die Höhe auf dem Graphen.", precision=2) 
some.tabelle([B1, B2, DundL], finished_file="build/tab2.tex", vars_name=[r"$\frac{B_1}{\sqrt{8 U_\text{B,1}}} / \si{\henry\volt\tothe{-\frac{1}{2}}}$",r"$\frac{B_2}{\sqrt{8 U_\text{B,2}}} / \si{\henry\volt\tothe{-\frac{1}{2}}}$", r"$\frac{D}{(L^2 + D^2)} / \si[per-mode=fraction]{\per\meter}$"], label_text="tab2", caption_text=r"Das Verhältnis des magnetischen Feldes durch die Wurzel der Beschleunigungsspannung aufgetragen gegen die Verschiebung $D$ durch die Summe des Wirkungsbereichs $L$ zum Quadrat und der Verschiebung $D$ zum Quadrat.", precision=2) 

#extra values
Ud5 = np.delete(Ud5, (0), 0)
dextra = np.delete(d, (0), 0)
#functions 
def gerade(a,b,c):
    return b*a+c

#Generate linReg-Plot

#U gegen d 
Steigung1, yWert1, r_value1, p_value1, err1= stats.linregress(Ud1/180, d)
Steigung2, yWert2, r_value2, p_value2, err2= stats.linregress(Ud2/230, d)
Steigung3, yWert3, r_value3, p_value3, err3= stats.linregress(Ud3/280, d)
Steigung4, yWert4, r_value4, p_value4, err4= stats.linregress(Ud4/330, d)
Steigung5, yWert5, r_value5, p_value5, err5= stats.linregress(Ud5/380, dextra)
#B gegen D und L 
Steigung6, yWert6, r_value6, p_value6, err6= stats.linregress(B1, DundL)
Steigung7, yWert7, r_value7, p_value7, err7= stats.linregress(B2, DundL)
plt.figure(1) 
newx1= np.linspace(Ud1[0]/180 -0.02,Ud1[-1]/180+0.02, num=1000)
newx2= np.linspace(Ud2[0]/230-0.02,Ud2[-1]/230+0.02, num=1000)
newx3= np.linspace(Ud3[0]/280-0.02,Ud3[-1]/280+0.02, num=1000)
newx4= np.linspace(Ud4[0]/330-0.02,Ud4[-1]/330+0.02, num=1000)
newx5= np.linspace(Ud5[0]/380-0.02,Ud5[-1]/380+0.02, num=1000)
newx6= np.linspace(B1[0]-5e-7,B1[-1]+5e-7, num=1000)
newx7= np.linspace(B2[0]-5e-7,B2[-1]+5e-7, num=1000)
plt.plot(Ud1/180, d, "xr", label=r"$U_\text{d, 1}/U_\text{B, 1}$")
plt.plot(Ud2/230, d, "xb", label=r"$U_\text{d, 2}/U_\text{B, 2}$")
plt.plot(Ud3/280, d, "xg", label=r"$U_\text{d, 3}/U_\text{B, 3}$")
plt.plot(Ud4/330, d, "xy", label=r"$U_\text{d, 4}/U_\text{B, 4}$")
plt.plot(Ud5/380, dextra, "xk", label=r"$U_\text{d, 5}/U_\text{B, 5}$")
plt.plot(newx1, gerade(newx1, Steigung1, yWert1), "r", linewidth=1.0)
plt.plot(newx2, gerade(newx2, Steigung2, yWert2), "b", linewidth=1.0)
plt.plot(newx3, gerade(newx3, Steigung3, yWert3), "g", linewidth=1.0)
plt.plot(newx4, gerade(newx4, Steigung4, yWert4), "y", linewidth=1.0)
plt.plot(newx5, gerade(newx5, Steigung5, yWert5), "k", linewidth=1.0)
plt.xlabel(r"$\frac{U_\text{d}}{U_\text{B}}$")
plt.ylabel(r"D / \si{\centi\meter}")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf") 

plt.figure(2) 
plt.plot(B1, DundL, "xr" )
plt.plot(B2, DundL, "xk")
plt.plot(newx6, gerade(newx6, Steigung6, yWert6), "r", label=r"$\frac{B_1}{\sqrt{8 U_\text{B,1}}}$", linewidth=1.0)
plt.plot(newx7, gerade(newx7, Steigung7, yWert7), "k", label=r"$\frac{B_2}{\sqrt{8 U_\text{B,2}}}$" ,  linewidth=1.0)
plt.xlabel(r"$\frac{B}{\sqrt{8 U_\text{B}}} / \si{\henry\volt\tothe{-\frac{1}{2}}}$")
plt.ylabel(r"$\frac{D}{L^2+D^2} / \si{\per\meter}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot2.pdf") 


#Generate curve-fit-Plot 
Steigungexp = np.array([Steigung1, Steigung2, Steigung3, Steigung4, Steigung5])
errexp = np.array([err1, err2, err3, err4, err5])
Steigung_exp = unp.uarray(Steigungexp, errexp)
Steigungnew = ufloat(Steigungexp.mean(), Steigungexp.std())
dicke= 0.38 #centimeter
platte= 1.9 #centimeter
Länge= 14.3 #centimeter
Steigung_theo= platte/(2*dicke) *Länge
sin1= frequenz1/np.array([0.5, 1, 2, 3])
sinmit= ufloat(sin1.mean(), sin1.std())

#e/m 
em1= np.array([Steigung6**2, Steigung7**2])
em= ufloat(em1.mean(), em1.std())
Erde= 4*np.pi*1e-7* (8/np.sqrt(125))*(N/R)* I_hor/np.cos(phi/180*np.pi)
#save solution
file = open("build/solution.txt", "w")
file.write(f"Steigung_exp = {Steigung_exp} cm\nMittelwert Steigung = {Steigungnew} cm\nSteigung_theo = {Steigung_theo} cm\nSinusfrequenz pro Wert: {sin1}\n Hz Sinus Mittelwert= {sinmit} Hz\ne0/m0 = {em}\nErdmagnetfeld: B = {Erde}")
file.close()
