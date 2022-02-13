* NMOS Current Mirrors
* LPA 13-Feb-2022

.option scale=1e-6
* Include SkyWater sky130 device models
.lib "/home/louis/git/sky130/skywater-pdk-libs-sky130_fd_pr/models/sky130.lib.spice" tt

* simple current mirror
xm1	o1 g1 0 0 	sky130_fd_pr__nfet_01v8_lvt w=1 l=0.15
xm2	g1 g1 0 0 	sky130_fd_pr__nfet_01v8_lvt w=1 l=0.15

* ideal bias for M2
I1	vdd1 g1  	50u

* set supply voltage
V1	vdd1 0		dc=1.8

* use voltage-controlled voltage source to allow a single sweep variable
Eo1	o1 o11 x1 0	1

* dummy voltage source so we can measure current
Vo1	o11 0		dc=0

* cascode current mirror (not so good bias)
xm3	d2 g2 0 0	sky130_fd_pr__nfet_01v8_lvt w=1 l=0.15
xm4     g2 g2 0 0	sky130_fd_pr__nfet_01v8_lvt w=1 l=0.15
xm5     o2 g3 d2 0	sky130_fd_pr__nfet_01v8_lvt w=1 l=0.15
xm6     g3 g3 g2 0	sky130_fd_pr__nfet_01v8_lvt w=1 l=0.15

* ideal bias
I2	vdd2 g3		50u

* set supply voltage
V2	vdd2 0		dc=1.8

* use voltage-controlled voltage source to allow a single sweep variable
Eo2	o2 o22 x1 0	1

* dummy voltage source so we can measure current
Vo2	o22 0		dc=0

* swept dc voltage source for both current mirrors
Vout 	x1 0 		dc=0.9

.control
* delete all previous plots so the plot numbering is deterministic
destroy all

* sweep output voltage and observe the output current
dc Vout 0 1.8 1m

plot (-i(Vo1)) (-i(Vo2)) (-i(V2))

.endc

.end
