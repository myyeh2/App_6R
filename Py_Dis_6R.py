
## C:\2302\Misc_14\Py_Dis_6R

import numpy as np 
import matplotlib.pyplot as plt  

x = np.arange(0, 50.5, 0.5)  

y0 = [   1.0000,         0.9397,         0.7718,         0.5246,         0.2339,
        -0.0617,        -0.3259,        -0.5295,        -0.6531,        -0.6888,
        -0.6399,        -0.5194,        -0.3477,        -0.1489,         0.0514,
         0.2299,         0.3673,         0.4507,         0.4741,         0.4394,
         0.3550,         0.2347,         0.0959,        -0.0433,        -0.1660,
        -0.2589,        -0.3134,        -0.3261,        -0.2992,        -0.2391,
        -0.1557,        -0.0606,         0.0340,         0.1171,         0.1799,
         0.2164,         0.2245,         0.2052,         0.1629,         0.1046,
         0.0384,        -0.0271,        -0.0840,        -0.1263,        -0.1502,
        -0.1542,        -0.1397,        -0.1098,        -0.0694,        -0.0240,
         0.0206,         0.0592,         0.0878,         0.1037,         0.1061,
         0.0957,         0.0746,         0.0464,         0.0149,        -0.0159,
        -0.0423,        -0.0615,        -0.0719,        -0.0728,        -0.0651,
        -0.0503,        -0.0307,        -0.0091,         0.0119,         0.0298,
         0.0428,         0.0496,         0.0501,         0.0445,         0.0341,
         0.0205,         0.0055,        -0.0090,        -0.0212,        -0.0299,
        -0.0343,        -0.0344,        -0.0303,        -0.0230,        -0.0135,
        -0.0032,         0.0066,         0.0149,         0.0208,         0.0237,
         0.0236,         0.0207,         0.0156,         0.0090,         0.0019,
        -0.0049,        -0.0106,        -0.0145,        -0.0164,        -0.0162,
        -0.0141,  ]  

y1 = [   2.0000,         1.8798,         1.5469,         1.0582,         0.4840,
        -0.1015,        -0.6285,        -1.0396,        -1.2953,        -1.3773,
        -1.2892,        -1.0546,        -0.7129,        -0.3133,         0.0917,
         0.4531,         0.7314,         0.9000,         0.9481,         0.8799,
         0.7130,         0.4752,         0.2004,        -0.0762,        -0.3218,
        -0.5099,        -0.6227,        -0.6527,        -0.6028,        -0.4851,
        -0.3190,        -0.1281,         0.0627,         0.2307,         0.3577,
         0.4319,         0.4489,         0.4112,         0.3279,         0.2125,
         0.0811,        -0.0493,        -0.1636,        -0.2494,        -0.2988,
        -0.3089,        -0.2814,        -0.2227,        -0.1421,        -0.0511,
         0.0387,         0.1167,         0.1746,         0.2070,         0.2122,
         0.1919,         0.1505,         0.0945,         0.0319,        -0.0296,
        -0.0826,        -0.1216,        -0.1431,        -0.1459,        -0.1312,
        -0.1020,        -0.0630,        -0.0197,         0.0226,         0.0587,
         0.0850,         0.0991,         0.1002,         0.0894,         0.0689,
         0.0418,         0.0120,        -0.0169,        -0.0415,        -0.0592,
        -0.0685,        -0.0689,        -0.0611,        -0.0466,        -0.0278,
        -0.0072,         0.0127,         0.0294,         0.0413,         0.0473,
         0.0473,         0.0416,         0.0315,         0.0184,         0.0042,
        -0.0094,        -0.0207,        -0.0287,        -0.0327,        -0.0325,
        -0.0284,  ] 

y2 = [   3.0000,         2.8195,         2.3187,         1.5828,         0.7179,
        -0.1632,        -0.9544,        -1.5691,        -1.9484,        -2.0661,
        -1.9291,        -1.5740,        -1.0605,        -0.4622,         0.1431,
         0.6830,         1.0987,         1.3507,         1.4222,         1.3193,
         1.0679,         0.7099,         0.2963,        -0.1195,        -0.4878,
        -0.7688,        -0.9360,        -0.9788,        -0.9019,        -0.7242,
        -0.4747,        -0.1888,         0.0967,         0.3478,         0.5376,
         0.6484,         0.6733,         0.6164,         0.4908,         0.3171,
         0.1195,        -0.0764,        -0.2476,        -0.3757,        -0.4490,
        -0.4631,        -0.4211,        -0.3325,        -0.2115,        -0.0751,
         0.0593,         0.1760,         0.2624,         0.3107,         0.3183,
         0.2876,         0.2251,         0.1409,         0.0467,        -0.0454,
        -0.1249,        -0.1831,        -0.2150,        -0.2188,        -0.1963,
        -0.1523,        -0.0938,        -0.0288,         0.0344,         0.0885,
         0.1278,         0.1487,         0.1503,         0.1340,         0.1030,
         0.0623,         0.0175,        -0.0259,        -0.0627,        -0.0891,
        -0.1028,        -0.1032,        -0.0914,        -0.0696,        -0.0413,
        -0.0104,         0.0193,         0.0443,         0.0621,         0.0710,
         0.0709,         0.0623,         0.0470,         0.0274,         0.0061,
        -0.0143,        -0.0313,        -0.0432,        -0.0491,        -0.0486,
        -0.0425,  ]  

plt.figure( figsize = (8, 4) )  
plt.subplots_adjust(bottom = 0.2, left = 0.2) 

plt.plot(x, y0, 'r-', label = r'$Pt-0$', lw = 3)  
plt.plot(x, y1, 'g-', label = r'$Pt-1$', lw = 3) 
plt.plot(x, y2, 'b-', label = r'$Pt-2$', lw = 3)  

plt.xlabel(r'$Time-Period(Sec)$').set_fontsize(16)  
plt.ylabel(r'$Displacement$').set_fontsize(16)  
plt.title(r'$**Time-Disp-Relationship$**').set_fontsize(16)  

plt.grid(axis = 'both')  
plt.legend(loc = 'best')  

plt.show()  
