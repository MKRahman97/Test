import numpy as np
from scipy.signal import chirp
import matplotlib.pyplot as plt
import numexpr as ne

outfile = r'C:\Users\Mohammed\OneDrive - University of Warwick\Mass spec\Oligonucleotide\decaying.svg'

plt.rcParams.update({'font.size': 22, 'font.weight': 'bold', 'font.family': 'Arial', 'mathtext.default': 'regular', 'axes.linewidth': 3,
                     'axes.labelweight': 'bold', 'xtick.major.size': 10, 'xtick.major.width': 5, 'xtick.minor.size': 10, 'xtick.minor.width': 5,
                     'ytick.major.size': 10, 'ytick.major.width': 5, 'ytick.minor.size': 10, 'ytick.minor.width': 5})

plt.axis('off')

T = 5
n = 1000
t = np.linspace(0, T, n, endpoint=False)
f0 = 9
f1 = 1
y = chirp(t, f0, T, f1, phi=2*np.pi, method='logarithmic')
# plt.plot(t, y, color='k', lw = 2.3)

# plt.show()
# plt.savefig(outfile)


SAMPLE_TIME = 20
SAMPLE_RATE = 0.1
x = np.arange(0, SAMPLE_TIME, SAMPLE_RATE)
damping_coefficent = 0.1
w = 1*np.pi
el =  np.exp(-x*damping_coefficent) * np.cos(w * x)
plt.plot(x, el, color='k', lw = 2.3)

plt.show()
# plt.savefig(outfile)
