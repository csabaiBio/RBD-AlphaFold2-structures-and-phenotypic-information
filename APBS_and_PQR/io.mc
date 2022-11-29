##############################################################################
# MC-shell I/O capture file.
# Creation Date and Time:  Mon Nov 28 23:24:08 2022

##############################################################################
Hello world from PE 0
Vnm_tstart: starting timer 26 (APBS WALL CLOCK)..
NOsh_parseInput:  Starting file parsing...
NOsh: Parsing READ section
NOsh: Storing molecule 0 path ./test_pqr/rot-Alpha_RBD_331_531_A344C.pdb.pqr
NOsh: Done parsing READ section
NOsh: Done parsing READ section (nmol=1, ndiel=0, nkappa=0, ncharge=0, npot=0)
NOsh: Parsing ELEC section
NOsh_parseMG: Parsing parameters for MG calculation
NOsh_parseMG:  Parsing dime...
PBEparm_parseToken:  trying dime...
MGparm_parseToken:  trying dime...
NOsh_parseMG:  Parsing cglen...
PBEparm_parseToken:  trying cglen...
MGparm_parseToken:  trying cglen...
NOsh_parseMG:  Parsing fglen...
PBEparm_parseToken:  trying fglen...
MGparm_parseToken:  trying fglen...
NOsh_parseMG:  Parsing cgcent...
PBEparm_parseToken:  trying cgcent...
MGparm_parseToken:  trying cgcent...
NOsh_parseMG:  Parsing fgcent...
PBEparm_parseToken:  trying fgcent...
MGparm_parseToken:  trying fgcent...
NOsh_parseMG:  Parsing lpbe...
PBEparm_parseToken:  trying lpbe...
NOsh: parsed lpbe
NOsh_parseMG:  Parsing bcfl...
PBEparm_parseToken:  trying bcfl...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing pdie...
PBEparm_parseToken:  trying pdie...
NOsh_parseMG:  Parsing sdie...
PBEparm_parseToken:  trying sdie...
NOsh_parseMG:  Parsing chgm...
PBEparm_parseToken:  trying chgm...
MGparm_parseToken:  trying chgm...
NOsh_parseMG:  Parsing mol...
PBEparm_parseToken:  trying mol...
NOsh_parseMG:  Parsing srfm...
PBEparm_parseToken:  trying srfm...
NOsh_parseMG:  Parsing srad...
PBEparm_parseToken:  trying srad...
NOsh_parseMG:  Parsing swin...
PBEparm_parseToken:  trying swin...
NOsh_parseMG:  Parsing temp...
PBEparm_parseToken:  trying temp...
NOsh_parseMG:  Parsing sdens...
PBEparm_parseToken:  trying sdens...
NOsh_parseMG:  Parsing calcenergy...
PBEparm_parseToken:  trying calcenergy...
NOsh_parseMG:  Parsing calcforce...
PBEparm_parseToken:  trying calcforce...
NOsh_parseMG:  Parsing write...
PBEparm_parseToken:  trying write...
NOsh_parseMG:  Parsing end...
MGparm_check:  checking MGparm object of type 1.
NOsh:  nlev = 4, dime = (129, 161, 161)
NOsh: Done parsing ELEC section (nelec = 1)
NOsh: Done parsing file (got QUIT)
Valist_readPQR: Counted 3117 atoms
Valist_getStatistics:  Max atom coordinate:  (-10.506, 54.897, 54.831)
Valist_getStatistics:  Min atom coordinate:  (-51.918, 5.078, -6.43)
Valist_getStatistics:  Molecule center:  (-31.212, 29.9875, 24.2005)
NOsh_setupCalcMGAUTO(/home/runner/work/apbs/apbs/src/generic/nosh.c, 1868):  coarse grid center = -31.4855 29.9415 24.296
NOsh_setupCalcMGAUTO(/home/runner/work/apbs/apbs/src/generic/nosh.c, 1873):  fine grid center = -31.4855 29.9415 24.296
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1885):  Coarse grid spacing = 0.581493, 0.559651, 0.683188
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1887):  Fine grid spacing = 0.498305, 0.454206, 0.526875
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1889):  Displacement between fine and coarse grids = 0, 0, 0
NOsh:  2 levels of focusing with 0.85694, 0.811589, 0.771201 reductions
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1983):  starting mesh repositioning.
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1985):  coarse mesh center = -31.4855 29.9415 24.296
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1990):  coarse mesh upper corner = 5.73005 74.7135 78.951
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1995):  coarse mesh lower corner = -68.701 -14.8305 -30.359
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2000):  initial fine mesh upper corner = 0.406 66.278 66.446
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2005):  initial fine mesh lower corner = -63.377 -6.395 -17.854
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2066):  final fine mesh upper corner = 0.406 66.278 66.446
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2071):  final fine mesh lower corner = -63.377 -6.395 -17.854
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalc:  Mapping ELEC statement 0 (1) to calculation 1 (2)
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 41.1008
Vpbe_ctor2:  solute dimensions = 43.821 x 52.693 x 64.183
Vpbe_ctor2:  solute charge = 4
Vpbe_ctor2:  bulk ionic strength = 0.15
Vpbe_ctor2:  xkappa = 0.125256
Vpbe_ctor2:  Debye length = 7.98362
Vpbe_ctor2:  zkappa2 = 1.22376
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (54.192, 62.599, 74.041)
Vclist_setupGrid:  Grid lower corner = (-58.308, -1.312, -12.82)
Vclist_assignAtoms:  Have 4854408 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 0.512353
Vpmg_fillco:  done filling coefficient arrays
Vpmg_fillco:  filling boundary arrays
Vpmg_fillco:  done filling boundary arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 1.210188e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (129, 161, 161)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 9.897200e-02
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (065, 081, 081)
Vbuildops: Galer: (033, 041, 041)
Vbuildops: Galer: (017, 021, 021)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 5.449480e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.943053e+00
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 9.980806e-02
Vprtstp: contraction number = 9.980806e-02
Vprtstp: iteration = 2
Vprtstp: relative residual = 1.369802e-02
Vprtstp: contraction number = 1.372436e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 2.500580e-03
Vprtstp: contraction number = 1.825505e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 5.476660e-04
Vprtstp: contraction number = 2.190156e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 1.290252e-04
Vprtstp: contraction number = 2.355910e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 3.797423e-05
Vprtstp: contraction number = 2.943164e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 9.317254e-06
Vprtstp: contraction number = 2.453573e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 3.193744e-06
Vprtstp: contraction number = 3.427774e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 7.892862e-07
Vprtstp: contraction number = 2.471351e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 2.641947e+00
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 3.346129e+00
Vpmg_setPart:  lower corner = (-68.701, -14.8305, -30.359)
Vpmg_setPart:  upper corner = (5.73005, 74.7135, 78.951)
Vpmg_setPart:  actual minima = (-68.701, -14.8305, -30.359)
Vpmg_setPart:  actual maxima = (5.73005, 74.7135, 78.951)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 1.000000e-06
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 7.000000e-06
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 41.1008
Vpbe_ctor2:  solute dimensions = 43.821 x 52.693 x 64.183
Vpbe_ctor2:  solute charge = 4
Vpbe_ctor2:  bulk ionic strength = 0.15
Vpbe_ctor2:  xkappa = 0.125256
Vpbe_ctor2:  Debye length = 7.98362
Vpbe_ctor2:  zkappa2 = 1.22376
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (54.192, 62.599, 74.041)
Vclist_setupGrid:  Grid lower corner = (-58.308, -1.312, -12.82)
Vclist_assignAtoms:  Have 4854408 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_ctor2:  Filling boundary with old solution!
VPMG::focusFillBound -- New mesh mins = -63.377, -6.395, -17.854
VPMG::focusFillBound -- New mesh maxs = 0.406, 66.278, 66.446
VPMG::focusFillBound -- Old mesh mins = -68.701, -14.8305, -30.359
VPMG::focusFillBound -- Old mesh maxs = 5.73005, 74.7135, 78.951
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 0.497293
Vpmg_fillco:  done filling coefficient arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 1.375073e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (129, 161, 161)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 9.375100e-02
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (065, 081, 081)
Vbuildops: Galer: (033, 041, 041)
Vbuildops: Galer: (017, 021, 021)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 5.242600e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 6.665689e+00
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 1.261612e-01
Vprtstp: contraction number = 1.261612e-01
Vprtstp: iteration = 2
Vprtstp: relative residual = 1.682411e-02
Vprtstp: contraction number = 1.333540e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 2.742730e-03
Vprtstp: contraction number = 1.630238e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 5.435707e-04
Vprtstp: contraction number = 1.981860e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 1.254143e-04
Vprtstp: contraction number = 2.307230e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 3.757274e-05
Vprtstp: contraction number = 2.995890e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 1.041694e-05
Vprtstp: contraction number = 2.772474e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 3.883410e-06
Vprtstp: contraction number = 3.727974e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 1.131038e-06
Vprtstp: contraction number = 2.912487e-01
Vprtstp: iteration = 10
Vprtstp: relative residual = 4.505224e-07
Vprtstp: contraction number = 3.983264e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 2.884839e+00
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 3.561687e+00
Vpmg_setPart:  lower corner = (-63.377, -6.395, -17.854)
Vpmg_setPart:  upper corner = (0.406, 66.278, 66.446)
Vpmg_setPart:  actual minima = (-63.377, -6.395, -17.854)
Vpmg_setPart:  actual maxima = (0.406, 66.278, 66.446)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 1.000000e-06
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 1.000000e-05
Vgrid_writeDX:  Opening virtual socket...
Vgrid_writeDX:  Writing to virtual socket...
Vgrid_writeDX:  Writing comments for ASC format.
Vnm_tstop: stopping timer 26 (APBS WALL CLOCK).  CPU TIME = 1.067831e+01
##############################################################################
# MC-shell I/O capture file.
# Creation Date and Time:  Mon Nov 28 23:36:16 2022

##############################################################################
Hello world from PE 0
Vnm_tstart: starting timer 26 (APBS WALL CLOCK)..
NOsh_parseInput:  Starting file parsing...
NOsh: Parsing READ section
NOsh: Storing molecule 0 path ./test_pqr/rot-Alpha_RBD_331_531_A344C.pdb.pqr
NOsh: Done parsing READ section
NOsh: Done parsing READ section (nmol=1, ndiel=0, nkappa=0, ncharge=0, npot=0)
NOsh: Parsing ELEC section
NOsh_parseMG: Parsing parameters for MG calculation
NOsh_parseMG:  Parsing dime...
PBEparm_parseToken:  trying dime...
MGparm_parseToken:  trying dime...
NOsh_parseMG:  Parsing cglen...
PBEparm_parseToken:  trying cglen...
MGparm_parseToken:  trying cglen...
NOsh_parseMG:  Parsing fglen...
PBEparm_parseToken:  trying fglen...
MGparm_parseToken:  trying fglen...
NOsh_parseMG:  Parsing cgcent...
PBEparm_parseToken:  trying cgcent...
MGparm_parseToken:  trying cgcent...
NOsh_parseMG:  Parsing fgcent...
PBEparm_parseToken:  trying fgcent...
MGparm_parseToken:  trying fgcent...
NOsh_parseMG:  Parsing lpbe...
PBEparm_parseToken:  trying lpbe...
NOsh: parsed lpbe
NOsh_parseMG:  Parsing bcfl...
PBEparm_parseToken:  trying bcfl...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing pdie...
PBEparm_parseToken:  trying pdie...
NOsh_parseMG:  Parsing sdie...
PBEparm_parseToken:  trying sdie...
NOsh_parseMG:  Parsing chgm...
PBEparm_parseToken:  trying chgm...
MGparm_parseToken:  trying chgm...
NOsh_parseMG:  Parsing mol...
PBEparm_parseToken:  trying mol...
NOsh_parseMG:  Parsing srfm...
PBEparm_parseToken:  trying srfm...
NOsh_parseMG:  Parsing srad...
PBEparm_parseToken:  trying srad...
NOsh_parseMG:  Parsing swin...
PBEparm_parseToken:  trying swin...
NOsh_parseMG:  Parsing temp...
PBEparm_parseToken:  trying temp...
NOsh_parseMG:  Parsing sdens...
PBEparm_parseToken:  trying sdens...
NOsh_parseMG:  Parsing calcenergy...
PBEparm_parseToken:  trying calcenergy...
NOsh_parseMG:  Parsing calcforce...
PBEparm_parseToken:  trying calcforce...
NOsh_parseMG:  Parsing write...
PBEparm_parseToken:  trying write...
NOsh_parseMG:  Parsing end...
MGparm_check:  checking MGparm object of type 1.
NOsh:  nlev = 4, dime = (129, 161, 161)
NOsh: Done parsing ELEC section (nelec = 1)
NOsh: Done parsing file (got QUIT)
Valist_readPQR: Counted 3117 atoms
Valist_getStatistics:  Max atom coordinate:  (-10.506, 54.897, 54.831)
Valist_getStatistics:  Min atom coordinate:  (-51.918, 5.078, -6.43)
Valist_getStatistics:  Molecule center:  (-31.212, 29.9875, 24.2005)
NOsh_setupCalcMGAUTO(/home/runner/work/apbs/apbs/src/generic/nosh.c, 1868):  coarse grid center = -31.4855 29.9415 24.296
NOsh_setupCalcMGAUTO(/home/runner/work/apbs/apbs/src/generic/nosh.c, 1873):  fine grid center = -31.4855 29.9415 24.296
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1885):  Coarse grid spacing = 0.581493, 0.559651, 0.683188
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1887):  Fine grid spacing = 0.498305, 0.454206, 0.526875
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1889):  Displacement between fine and coarse grids = 0, 0, 0
NOsh:  2 levels of focusing with 0.85694, 0.811589, 0.771201 reductions
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1983):  starting mesh repositioning.
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1985):  coarse mesh center = -31.4855 29.9415 24.296
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1990):  coarse mesh upper corner = 5.73005 74.7135 78.951
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 1995):  coarse mesh lower corner = -68.701 -14.8305 -30.359
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2000):  initial fine mesh upper corner = 0.406 66.278 66.446
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2005):  initial fine mesh lower corner = -63.377 -6.395 -17.854
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2066):  final fine mesh upper corner = 0.406 66.278 66.446
NOsh_setupCalcMGAUTO (/home/runner/work/apbs/apbs/src/generic/nosh.c, 2071):  final fine mesh lower corner = -63.377 -6.395 -17.854
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalc:  Mapping ELEC statement 0 (1) to calculation 1 (2)
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 41.1008
Vpbe_ctor2:  solute dimensions = 43.821 x 52.693 x 64.183
Vpbe_ctor2:  solute charge = 4
Vpbe_ctor2:  bulk ionic strength = 0.15
Vpbe_ctor2:  xkappa = 0.125256
Vpbe_ctor2:  Debye length = 7.98362
Vpbe_ctor2:  zkappa2 = 1.22376
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (54.192, 62.599, 74.041)
Vclist_setupGrid:  Grid lower corner = (-58.308, -1.312, -12.82)
Vclist_assignAtoms:  Have 4854408 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 0.501259
Vpmg_fillco:  done filling coefficient arrays
Vpmg_fillco:  filling boundary arrays
Vpmg_fillco:  done filling boundary arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 1.174026e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (129, 161, 161)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 1.014650e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (065, 081, 081)
Vbuildops: Galer: (033, 041, 041)
Vbuildops: Galer: (017, 021, 021)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 5.279520e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.891231e+00
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 9.980806e-02
Vprtstp: contraction number = 9.980806e-02
Vprtstp: iteration = 2
Vprtstp: relative residual = 1.369802e-02
Vprtstp: contraction number = 1.372436e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 2.500580e-03
Vprtstp: contraction number = 1.825505e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 5.476660e-04
Vprtstp: contraction number = 2.190156e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 1.290252e-04
Vprtstp: contraction number = 2.355910e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 3.797423e-05
Vprtstp: contraction number = 2.943164e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 9.317254e-06
Vprtstp: contraction number = 2.453573e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 3.193744e-06
Vprtstp: contraction number = 3.427774e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 7.892862e-07
Vprtstp: contraction number = 2.471351e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 2.641289e+00
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 3.330897e+00
Vpmg_setPart:  lower corner = (-68.701, -14.8305, -30.359)
Vpmg_setPart:  upper corner = (5.73005, 74.7135, 78.951)
Vpmg_setPart:  actual minima = (-68.701, -14.8305, -30.359)
Vpmg_setPart:  actual maxima = (5.73005, 74.7135, 78.951)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 8.000000e-06
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 41.1008
Vpbe_ctor2:  solute dimensions = 43.821 x 52.693 x 64.183
Vpbe_ctor2:  solute charge = 4
Vpbe_ctor2:  bulk ionic strength = 0.15
Vpbe_ctor2:  xkappa = 0.125256
Vpbe_ctor2:  Debye length = 7.98362
Vpbe_ctor2:  zkappa2 = 1.22376
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (54.192, 62.599, 74.041)
Vclist_setupGrid:  Grid lower corner = (-58.308, -1.312, -12.82)
Vclist_assignAtoms:  Have 4854408 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_ctor2:  Filling boundary with old solution!
VPMG::focusFillBound -- New mesh mins = -63.377, -6.395, -17.854
VPMG::focusFillBound -- New mesh maxs = 0.406, 66.278, 66.446
VPMG::focusFillBound -- Old mesh mins = -68.701, -14.8305, -30.359
VPMG::focusFillBound -- Old mesh maxs = 5.73005, 74.7135, 78.951
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 0.523231
Vpmg_fillco:  done filling coefficient arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 1.412531e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (129, 161, 161)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 9.922800e-02
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (065, 081, 081)
Vbuildops: Galer: (033, 041, 041)
Vbuildops: Galer: (017, 021, 021)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 5.286670e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 6.666744e+00
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 1.261612e-01
Vprtstp: contraction number = 1.261612e-01
Vprtstp: iteration = 2
Vprtstp: relative residual = 1.682411e-02
Vprtstp: contraction number = 1.333540e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 2.742730e-03
Vprtstp: contraction number = 1.630238e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 5.435707e-04
Vprtstp: contraction number = 1.981860e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 1.254143e-04
Vprtstp: contraction number = 2.307230e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 3.757274e-05
Vprtstp: contraction number = 2.995890e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 1.041694e-05
Vprtstp: contraction number = 2.772474e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 3.883410e-06
Vprtstp: contraction number = 3.727974e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 1.131038e-06
Vprtstp: contraction number = 2.912487e-01
Vprtstp: iteration = 10
Vprtstp: relative residual = 4.505224e-07
Vprtstp: contraction number = 3.983264e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 2.925667e+00
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 3.614607e+00
Vpmg_setPart:  lower corner = (-63.377, -6.395, -17.854)
Vpmg_setPart:  upper corner = (0.406, 66.278, 66.446)
Vpmg_setPart:  actual minima = (-63.377, -6.395, -17.854)
Vpmg_setPart:  actual maxima = (0.406, 66.278, 66.446)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 1.000000e-06
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 7.000000e-06
Vgrid_writeDX:  Opening virtual socket...
Vgrid_writeDX:  Writing to virtual socket...
Vgrid_writeDX:  Writing comments for ASC format.
Vnm_tstop: stopping timer 26 (APBS WALL CLOCK).  CPU TIME = 1.072646e+01
