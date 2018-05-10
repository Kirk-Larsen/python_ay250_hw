import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np

#create figure to display the active plot
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')

#create part of a grayscale which we can traverse through in different ways
#move through grayscale linearly
grays_linear = list(np.linspace(0.2, 0.8, 50))

#move through grayscale cubicly
grays_cubic = [x**3 for x in np.linspace(0.2,0.8,50)]

#jump between the two extremes of grayscale (binary pattern/square wave)
grays_binary = [0.2]*25 + [0.8]*25

#create cycle iterator to return elements from the grayscale concatenated with its reversed self
#assign desired pattern (linear, cubic, binary) below
grays = cycle(grays_linear + list(reversed(grays_linear)))

#create a linear space of values for the outer annulus radius which we can traverse through 
sizes = list(np.linspace(0.2, 0.25, 50))

#create cycle iterator to return elements from the list of radii concatenated with its reversed self
sizes = cycle(sizes + list(reversed(sizes)))

#create active figure using a loop
while True:

	#use __next__ method to retrieve next item (grayscale value) from cycle iterator
    color = (next(grays), ) * 3 + (1., )

	#use __next__ method to retrieve next item (outer radius) from cycle iterator
    size = next(sizes)

    #remove x-axis tick labels
    ax.set_xticklabels([])

	#plot annulus, pause for 0.01 seconds
    circle1 = plt.Circle((0.5, 0.5), 0.15, color='black')
    circle2 = plt.Circle((0.5, 0.5), size, color=color)
    ax.add_artist(circle2)
    ax.add_artist(circle1)
    plt.axis('off')
    plt.pause(0.01)
    ax.clear()