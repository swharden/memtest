# The Patch-Clamp Membrane Test

This repository is a personal collection of notes and resources related to membrane tests (analytical methods performed on electrical traces to calculate membrane parameters of cells). It is currently being developed as part of a multi-part blog post on www.swharden.com

## Single Electrode Whole-Cell Voltage Clamp Circuit

**I created this model to simulate a patch-clamped neuron in whole-cell configuration.** Square voltage-clamp pulses mimic a membrane test protocol. By analyzing the clamp current trace alone I can derive values for Ra (access resistance), Rm (membrane resistance), and Cm (cell capacitance).

<div align="center">

![](dev/diagram/whole-cell-voltage-clamp-diagram.png)

![](models/single-electrode-advanced/voltage-clamp-circuit.png)

![](models/single-electrode-advanced/voltage-clamp-simulation.png)

</div>


## Two Electrode Voltage Clamp Circuit

**I created this model to simulate a giant squid axon studied with a two-electrode system.** It's not particularly useful other than as a thought exercise. By clamping between two different voltages you can measure the difference in current passing through the stimulation resistor to estimate the neuron's membrane resistance.

<div align="center">

![](models/two-electrode/VC-two-electrode-circuit.png)

![](models/two-electrode/VC-two-electrode-simulation.png)

</div>

## Analyze LTSpice Data with Python

```python
import ltspice
l = ltspice.Ltspice("voltage-clamp.raw")
l.parse()

times = l.getTime() * 1e3 # ms
Vcell = l.getData('V(n007)') * 1e3  # mV
Vcommand = l.getData('V(n006)') * 1e3  # mV
Iclamp = l.getData('I(Rf)') * 1e12  # pA
```

<div align="center">

![](models/single-electrode-advanced/voltage-clamp-simple-fig1.png)

</div>

```python
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
```