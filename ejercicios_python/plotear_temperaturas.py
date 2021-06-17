#plotear_temperaturas.py

import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('Data/Temperaturas.npy')

plt.hist(temperaturas, bins=80)
