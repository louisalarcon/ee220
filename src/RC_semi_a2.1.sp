* Semiconductor resistor characteristics
* LPA 05 Aug 2020

.options savecurrents seed=random

* Polysilicon resistor models
.model rpoly_n R rsh=100 tc1=-800u tnom=27C
.model rpoly_p R rsh=180 tc1=200u tnom=27C


* MOM capacitor model
.model cmom C cj=50m tc1=30u tnom=27C 
.model cmsub C cj=30m tc1=25u tnom=27C

* Capacitor with bottom-plate parasitic capacitance
.subckt cm  top bottom sub  w=1000u l=2000u
C1		top bottom	cmom w={w} l={l}
Csub	bottom sub	cmsub w={w} l={l}
.ends

R1		in out		rpoly_n w=2u l=20u
X1		out 0 0		cm w=1000u l=2000u

Vs		in 0		dc 0 ac 1

.control

let mc_runs = 1000
let run = 1

define gauss(nom, var) (nom + nom*var * sgauss(0))

dowhile run <= mc_runs
	
	* mismatch
	alter @R1[l] = gauss(20u, 0.01)
	alter @R1[w] = gauss(2u, 0.01)
	
	let l1 = gauss(2000u, 0.01)
	alter @c.x1.c1[l] = l1
	alter @c.x1.csub[l] = l1

	let l2 = gauss(1000u, 0.01)
	alter @c.x1.c1[w] = l2
	alter @c.x1.csub[w] = l2

	* process
	altermod @rpoly_n[rsh] = gauss(100, 0.01)
	altermod @cmom[cj] = gauss(50m, 0.01)
	altermod @cmsub[cj] = gauss(30m, 0.01)

	ac dec 1000 10 10k
	echo {$run}
	meas ac fc WHEN vdb(out)=-3 FALL=1

	let R1 = @r1[r]
	let C1 = @c.x1.c1[cap]	
	set run = "$&run"
	
	echo {$run} {$&R1} {$&C1} {$&fc} >> mc_RC.dat

	let run = run + 1
end

.endc

.end
