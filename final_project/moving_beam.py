import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle

fig, ax = plt.subplots(figsize=(8, 8))

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
x_, y_ = np.meshgrid(x, y)

sigma = 0.5
mu_ = [x for x in np.linspace(3, 7, 40)]
mu_c = cycle(mu_ + list(reversed(mu_)))

ax = plt.gca()
while True:
    mu = next(mu_c)
    z = (1 / np.sqrt(2 * np.pi * sigma)) * np.exp(-((x_ - mu)**2 + (y_ - mu)**2) / (2 * sigma**2))
    plt.imshow(z)
    plt.pause(0.01)
    ax.clear()