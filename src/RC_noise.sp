* Resistor Noise Simulation
* LPA 13-Feb-2022

* A simple RC circuit
R1	1 2	1k
C1	2 0	1p
V1	1 0	dc=1 ac=1


.control
* delete all previous plots so the plot numbering is deterministic
destroy all

* set the output to power spectral density (V^2 or A^2) 
set sqrnoise

* run noise analysis
* note that the spectral density will be in a plot called 'noise 1'
* and the total integrated noise will be in a plot called 'noise 2'
noise v(2) v1 dec 1000 1 1e12

* change the value of the resistor and re-run the simulation
alter R1 10k
set sqrnoise
noise v(2) v1 dec 1000 1 1e12
* note that the spectral density will be in a plot called 'noise 3'
* and the total integrated noise will be in a plot called 'noise 4'

* return R1 to its previous value and change C1
alter R1 1k
alter C1 10p
noise v(2) v1 dec 1000 1 1e12
* note that the spectral density will be in a plot called 'noise 5'
* and the total integrated noise will be in a plot called 'noise 6'

* plot everything in one graph
plot noise1.onoise_spectrum noise3.onoise_spectrum noise5.onoise_spectrum xlog ylog

* print the total integrated output noise
print noise2.onoise_total noise4.onoise_total noise6.onoise_total

.endc

.end

