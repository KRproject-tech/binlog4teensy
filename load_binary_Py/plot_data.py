import numpy as np
import matplotlib.pyplot as plt
from scipy.io import savemat

import load_bin


# File name
file_name = 'data.log'


# Load data (assuming int16 type for binary data)
out = load_bin.load_bin( "./load/" + file_name, np.int16)

# Process time and data
time_m = out[:,0] / 1000  # [ms] -> [s]
d_time = np.diff( time_m)   # Time differences
time_m = d_time[0] * np.arange(1, len( time_m) + 1)

# Convert output data
out = out[:,1:] / 100  # [c] -> [-]

# Plotting
fig, ax = plt.subplots()

ax.plot( time_m, out, '-', linewidth=0.5, label="data")
ax.set_xlabel( r'Time $\mathrm{[s]}$', fontsize=15)
ax.set_ylabel( r'data $\mathrm{[-]}$', fontsize=15)
ax.set_xlim([time_m[0], time_m[-1]])
plt.legend( fontsize = 10)


# save 
save_data = {
    "time_m": time_m,
    "out": out
}


plt.savefig( "./save/fig/data.pdf")
savemat( "./save/NUM_DATA.mat", save_data)


plt.show()


