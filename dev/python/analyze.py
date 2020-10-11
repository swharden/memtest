import os
import ltspice
import matplotlib.pyplot as plt
import numpy as np

filePath = os.path.join(os.path.dirname(__file__), "voltage-clamp-simple.raw")
print("loading", filePath)
assert os.path.isfile(filePath)

l = ltspice.Ltspice(filePath)
l.parse()
print("NAMES:", ", ".join(l.getVariableNames()))

times = l.getTime() * 1e3  # ms
Vcell = l.getData('V(n003)') * 1e3  # mV
Vcommand = l.getData('V(vcmd)') * 1e3  # mV
Iclamp = l.getData('I(Rf)') * 1e12  # pA

ax1 = plt.subplot(211)
plt.grid(ls='--', alpha=.5)
plt.plot(times, Iclamp, 'r-')
plt.ylabel("Current (pA)")

plt.subplot(212, sharex=ax1)
plt.grid(ls='--', alpha=.5)
plt.plot(times, Vcell, label="Cell")
plt.plot(times, Vcommand, label="Clamp")
plt.ylabel("Potential (mV)")
plt.xlabel("Time (milliseconds)")
plt.legend()

plt.margins(0, .1)
plt.tight_layout()
plt.savefig(os.path.dirname(__file__) + "/voltage-clamp-simple-fig1.png")
# plt.show()
