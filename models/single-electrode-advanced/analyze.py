# read data from the LTSpice .raw file
import ltspice
l = ltspice.Ltspice("voltage-clamp.raw")
l.parse()

# obtain data by its identifier and scale it as desired
times = l.getTime() * 1e3 # ms
Vcell = l.getData('V(n007)') * 1e3  # mV
Vcommand = l.getData('V(n006)') * 1e3  # mV
Iclamp = l.getData('I(Rf)') * 1e12  # pA

# plot scaled simulation data
import matplotlib.pyplot as plt

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
plt.savefig("voltage-clamp-simple-fig1.png")
#plt.show()