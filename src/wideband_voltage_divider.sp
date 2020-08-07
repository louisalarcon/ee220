* Wideband Voltage Divider Circuit
* LPA 05 Aug 2020

.options savecurrents

R1		in out		900k
R2		out 0		100k

C1		in out	 	1.1111p
C2		out 0		10p

* increase C1 and see what happens
R1a		in outa		900k
R2a		outa 0		100k

C1a		in outa	 	1.6p
C2a		outa 0		10p

* decrease C1 and see what happens
R1b		in outb		900k
R2b		outb 0		100k

C1b		in outb	 	0.7p
C2b		outb 0		10p

* input square wave
V1		in 0		dc 1 ac 1 pulse(-1 1 0 0.1u 0.1u 5u 0.01m)

.control

ac dec 10 1 1G
plot vdb(out) vdb(outa) vdb(outb) 
wrdata testac.dat v(out) v(outa) v(outb)

tran 0.01u 0.03m
plot v(out) v(outa) v(outb)
wrdata testtran.dat v(out) v(outa) v(outb)

.endc

.end


