* NMOS Noise Characterization
* LPA 03 Oct 2021

.option scale=1e-6
* Include SkyWater sky130 device models
.lib "/home/louis/git/sky130/skywater-pdk-libs-sky130_fd_pr/models/sky130.lib.spice" tt

* instantiate the NMOSFET
xm1	d g 0 0 	sky130_fd_pr__nfet_01v8_lvt w=1 l=0.15
vd	d 0		dc=1.8
vg	g 0		dc=0.9 ac=1

* convert drain current into an output voltage for noise analysis
h1	out 0		vd 1

.control
* delete all previous plots so the plot numbering is deterministic
destroy all

* set the output to power spectral density (V^2 or A^2) 
set sqrnoise
noise v(out) vg dec 1000 1 1e12
* note that the spectral density will be in a plot called 'noise 1'
* and the total integrated noise will be in a plot called 'noise 2'

* increase the the gate voltage
alter vg dc=1.2
noise v(out) vg dec 1000 1 1e12
* note that the spectral density will be in a plot called 'noise 3'
* and the total integrated noise will be in a plot called 'noise 4'

* decrease the gate voltage
alter vg dc=0.6
noise v(out) vg dec 1000 1 1e12
* note that the spectral density will be in a plot called 'noise 5'
* and the total integrated noise will be in a plot called 'noise 6'

* plot everything in one graph
plot noise1.onoise_spectrum noise3.onoise_spectrum noise5.onoise_spectrum ylog xlog

* print the total integrated output noise
print noise2.onoise_total noise4.onoise_total noise6.onoise_total

.endc

.end
