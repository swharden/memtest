import os
import ltspice
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
np.set_printoptions(suppress=True)

l = ltspice.Ltspice(os.path.dirname(__file__) + "/voltage-clamp-simple.raw")
l.parse()

times = l.getTime() * 1e3  # ms
Iclamp = l.getData('I(Rf)') * 1e12  # pA

plt.figure(figsize=(6, 3))
plt.title("Irregularly Spaced Data")
plt.plot(times, Iclamp, '.-')
plt.savefig(os.path.dirname(__file__) + "/voltage-clamp-simple-fig3.png")
plt.show()

# interpolate data for 20 kHz sample rate
f = scipy.interpolate.interp1d(times, Iclamp)
pointCount = int((times[-1] - times[0]) * 20) + 1
times = np.linspace(times[0], times[-1], pointCount)
Iclamp = f(times)

plt.figure(figsize=(6, 3))
plt.grid(ls='--', alpha=.5)
plt.title("Interpolated 20kHz Signal")
plt.plot(times, Iclamp)
plt.savefig(os.path.dirname(__file__) + "/voltage-clamp-simple-fig4.png")

np.savetxt(os.path.dirname(__file__) + "/voltage-clamp-simple.csv", Iclamp)

plt.show()
