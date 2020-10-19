* MOS Characterization
* LPA 05 Aug 2020

.options savecurrents seed=random
.include '/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/45nm_NMOS_bulk69327_ff.pm'
.include '/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/45nm_NMOS_bulk69327_ss.pm'
.include '/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/45nm_NMOS_bulk69327.pm'

m1		d1 g1 0 0 		nmos w=1u l=45n
vgs		g1 0 			dc=1
vds		d1 0			dc=1

.control

altermod nmos file='/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/45nm_NMOS_bulk69327.pm'

dc vgs 0 1 0.01
wrdata nmos_transfer_tt.dat @m1[id]
dc vds 0 1 0.01 vgs 0.2 1 0.2
wrdata nmos_output_tt.dat @m1[id]

altermod nmos file='/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/45nm_NMOS_bulk69327_ff.pm'

dc vgs 0 1 0.01
wrdata nmos_transfer_ff.dat @m1[id]
dc vds 0 1 0.01 vgs 0.2 1 0.2
wrdata nmos_output_ff.dat @m1[id]

altermod nmos file='/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/45nm_NMOS_bulk69327_ss.pm'

dc vgs 0 1 0.01
wrdata nmos_transfer_ss.dat @m1[id]
dc vds 0 1 0.01 vgs 0.2 1 0.2
wrdata nmos_output_ss.dat @m1[id]

.endc

.end
