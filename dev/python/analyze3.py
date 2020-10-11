import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

sweep = np.loadtxt(os.path.dirname(__file__)+"/voltage-clamp-simple.csv")
times = np.arange(len(sweep)) / 20
sweepA = np.array(sweep[601:1100])
timesA = np.array(times[601:1100])
sweepB = np.array(sweep[1101:1600])
timesB = np.array(times[1101:1600])

plt.figure(figsize=(6, 3))
plt.ylabel("Clamp Current (pA)")
plt.xlabel("Sweep Time (milliseconds)")
plt.plot(times, sweep, 'k-', alpha=.2)
plt.plot(timesA, sweepA, 'b-', label="A")
plt.plot(timesB, sweepB, 'g-', label="B")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.dirname(__file__) + "/voltage-clamp-simple-fig5.png")
plt.close()

plt.figure(figsize=(6, 3))
plt.subplot(121)
plt.plot(sweepA, 'b')
plt.subplot(122)
plt.plot(sweepB, 'g')
plt.tight_layout()
plt.savefig(os.path.dirname(__file__) + "/voltage-clamp-simple-fig6.png")
plt.close()

# https://swharden.com/blog/2020-09-24-python-exponential-fit/


def monoExp(x, m, t, b):
    return m * np.exp(-t * x) + b


segTimes = np.arange(len(sweepA))/20
params, cv = scipy.optimize.curve_fit(
    monoExp, segTimes, sweepA, (2000, .1, 50))
mA, tA, bA = params
IpeakA = monoExp(-1/20, mA, tA, bA)
print(f"Segment A: tau={1/tA:.03f} ms, Iss={bA:.03f} pA, I0={IpeakA - bA:.03f} pA (Ipeak = {IpeakA:.03f} pA)")

segTimes = np.arange(len(sweepB))/20
params, cv = scipy.optimize.curve_fit(
    monoExp, segTimes, sweepB, (2000, .1, 50))
mB, tB, bB = params
IpeakB = monoExp(-1/20, mB, tB, bB)
print(f"Segment B: tau={1/tB:.03f} ms, Iss={bB:.03f} pA, I0={IpeakB - bB:.03f} pA (Ipeak = {IpeakB:.03f} pA)")

plt.figure(figsize=(6, 3))
plt.ylabel("Clamp Current (pA)")
plt.xlabel("Sweep Time (milliseconds)")
plt.plot(times, sweep, 'k-', alpha=.2)

plt.plot(timesA, sweepA, 'b-')
plt.plot(timesA, monoExp(segTimes, mA, tA, bA), 'r-')

plt.plot(timesB, sweepB, 'g-')

plt.axhline(bA, ls=':', color='b')
plt.axhline(bB, ls=':', color='g')

plt.tight_layout()
plt.savefig(os.path.dirname(__file__) + "/voltage-clamp-simple-fig7.png")

#plt.show()
