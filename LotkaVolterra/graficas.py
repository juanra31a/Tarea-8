import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

walk = np.loadtxt("valores.dat")

plt.scatter(walk[1,:],walk[0,:])
plt.xlabel('$\\alpha$')
plt.ylabel('$\\beta$')
plt.title('$\\alpha$ vs. $\\beta$')
plt.savefig("alphavsbeta.pdf")
plt.close()

plt.scatter(walk[2,:],walk[0,:])
plt.xlabel('$\gamma$')
plt.ylabel('$\\alpha$')
plt.title('$\\alpha$ vs. $\gamma$')
plt.savefig("alphavsgamma.pdf")
plt.close()

plt.scatter(walk[3,:],walk[0,:])
plt.xlabel('$\delta$')
plt.ylabel('$\\alpha$')
plt.title('$\\alpha$ vs. $\delta$')
plt.savefig("alphavsdelta.pdf")
plt.close()

plt.scatter(walk[3,:],walk[2,:])
plt.xlabel('$\gamma$')
plt.ylabel('$\delta$')
plt.title('$\gamma$ vs. $\delta$')
plt.savefig("gammavsdelta.pdf")
plt.close()

plt.scatter(np.log(walk[4,:]),walk[0,:])
plt.xlabel('$\chi^2$')
plt.ylabel('$\\alpha$')
plt.title('$\chi^2$ vs. $\\alpha$')
plt.savefig("x2vsalpha.pdf")
plt.close()

plt.scatter(np.log(walk[4,:]),walk[1,:])
plt.xlabel('$\chi^2$')
plt.ylabel('$\\beta$')
plt.title('$\chi^2$ vs. $\\beta$')
plt.savefig("x2vsbeta.pdf")
plt.close()

plt.scatter(np.log(walk[4,:]),walk[2,:])
plt.xlabel('$\chi^2$')
plt.ylabel('$\gamma$')
plt.title('$\chi^2$ vs. $\gamma$')
plt.savefig("x2vsgamma.pdf")
plt.close()

plt.scatter(np.log(walk[4,:]),walk[3,:])
plt.xlabel('$\chi^2$')
plt.ylabel('$\delta$')
plt.title('$\chi^2$ vs. $\delta$')
plt.savefig("x2vsdelta.pdf")
plt.close()