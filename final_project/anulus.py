import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np

#linear pattern
grays = list(np.linspace(0.2, 0.8, 50))

#cubic pattern
#grays = [x**3 for x in np.linspace(0.2,0.8,100)]

#square wave pattern
#grays = [0]*10 + [1]*10

grays = cycle(grays + list(reversed(grays)))

sizes = list(np.linspace(0.2, 0.25, 50))
sizes = cycle(sizes + list(reversed(sizes)))

fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')

while True:
    color = (next(grays), ) * 3 + (1., )
    size = next(sizes)
    circle1 = plt.Circle((0.5, 0.5), 0.15, color='black')
    circle2 = plt.Circle((0.5, 0.5), size, color=color)
    ax.add_artist(circle2)
    ax.add_artist(circle1)
    ax.set_xticklabels([])
    plt.axis('off')
    plt.pause(0.01)
    ax.clear()