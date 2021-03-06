import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

plt.rcParams.update({'font.size': 24})

lambda_, deg1_1, min1_1, deg1_2, min1_2,  deg2_1, min2_1, deg2_2, min2_2, deg3_1, min3_1, deg3_2, min3_2 = np.genfromtxt("data/data.txt", unpack=True)


# min to deg 
deg1_1 = deg1_1 + min1_1/60 
deg1_2 = deg1_2 + min1_2/60
deg2_1 = deg2_1 + min2_1/60
deg2_2 = deg2_2 + min2_2/60
deg3_1 = deg3_1 + min3_1/60
deg3_2 = deg3_2 + min3_2/60

winkel1 = 0.5*(deg1_1 - deg1_2)
winkel2 = 0.5*(deg2_1 - deg2_2) 
winkel3 = 0.5*(deg3_1 - deg3_2) 

winkel1 = np.deg2rad(winkel1)/5.11e-3
winkel2 = np.deg2rad(winkel2)/1.296e-3
winkel3 = np.deg2rad(winkel3)/1.36e-3

np.savetxt("data/winkel1.txt", winkel1)
np.savetxt("data/winkel2.txt", winkel2)
np.savetxt("data/winkel3.txt", winkel3)

plt.figure(figsize=(15,8))
plt.xlabel(r"$\lambda^2$ / $(\mathrm{\mu m})^2$")
plt.ylabel(r"$\frac{\theta}{\mathrm{d}}$ / $\frac{\mathrm{rad}}{\mathrm{m}}$")
plt.plot((lambda_**2)*1e12, winkel1, "x", mew=3, markersize=14, label="Reine Probe")
plt.plot((lambda_**2)*1e12, winkel2, "x", mew=3, markersize=14, label="Probe 1")
plt.plot((lambda_**2)*1e12, winkel3, "x", mew=3, markersize=14, label="Probe 2")
plt.legend(loc="best")
plt.grid()
plt.savefig("plots/AlleProben.pdf")

diff1 = np.abs(winkel2-winkel1) 
diff2 = np.abs(winkel3-winkel1)

np.savetxt("data/diff1.txt", diff1)
np.savetxt("data/diff2.txt", diff2)


N1 = 2.8e24
N2 = 1.2e24
n = 3.57
B = 392e-3


def mass(x, a):
    return a * x 

params1, cov1 = curve_fit(mass, lambda_**2, diff1, p0=[12e12] )

lambda_new = np.linspace(min(lambda_)-2e-6, max(lambda_)+0.5e-7, 100)
plt.figure(figsize=(15,8))
plt.xlabel(r"$\lambda^2$ / $(\mathrm{\mu m})^2$")
plt.ylabel(r"$\theta_\mathrm{frei,1}$ / $\frac{\mathrm{rad}}{\mathrm{m}}$")
plt.plot((lambda_**2)*1e12, diff1, "x", mew=3, markersize=14, label="Daten")
plt.plot((lambda_new**2)*1e12, mass(lambda_new**2, *params1), linewidth=5, label="Ausgleichsgerade")
plt.legend(loc="best")
plt.grid()
plt.savefig("plots/Probe1.pdf")

err1 = np.diag(np.sqrt(cov1))
a1 = ufloat(params1[0], err1[0])

mass1 = unp.sqrt(const.elementary_charge**3 *N1 *B / (8* np.pi**2 *const.epsilon_0 * const.speed_of_light**3 * n * a1))

params2, cov2 = curve_fit(mass, lambda_**2, diff2, p0=[12e12] )

plt.figure(figsize=(15,8))
plt.xlabel(r"$\lambda^2$ / $(\mathrm{\mu m})^2$")
plt.ylabel(r"$\theta_\mathrm{frei,2}$ / $\frac{\mathrm{rad}}{\mathrm{m}}$")
plt.plot((lambda_**2)*1e12, diff2, "x", mew=3, markersize=14, label="Daten")
plt.plot((lambda_new**2)*1e12, mass(lambda_new**2, *params2), linewidth=5, label="Ausgleichsgerade")
plt.legend(loc="best")
plt.grid()
plt.savefig("plots/Probe2.pdf")

err2 = np.diag(np.sqrt(cov2))
a2 = ufloat(params2[0], err2[0])

mass2 = unp.sqrt(const.elementary_charge**3 *N2 *B / (8* np.pi**2 *const.epsilon_0 * const.speed_of_light**3 * n * a2))

f=  open("plots/results.txt", "w")
f.write(f"Steigung 1: {a1}, Masse 1: {mass1/const.electron_mass}\n")
f.write(f"Steigung 2: {a2}, Masse 2: {mass2/const.electron_mass}")
f.close()