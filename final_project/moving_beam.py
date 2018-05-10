import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle

#create figure to display the active plot
fig, ax = plt.subplots(figsize=(8, 8))

#create 100 x 100 grid with values between 0 - 10
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
x_, y_ = np.meshgrid(x, y)

#define Gaussian standard deviation
sigma = 0.5

#define mean values for a beam moving in a diagonal pattern
#create cycle iterator to return elements from list of means concatenated with its reversed self 
#mu_ = list(np.linspace(3, 7, 40))
#mu_c = cycle(mu_ + list(reversed(mu_)))

#define mean values for a beam moving in a square pattern
#create cycle iterator to return elements from the concatenated lists of means
mu_1 = [[x, 3] for x in np.linspace(3, 7, 20)]
mu_2 = [[7, y] for y in np.linspace(3, 7, 20)]
mu_3 = [[x, 7] for x in reversed(np.linspace(3, 7, 20))]
mu_4 = [[3, y] for y in reversed(np.linspace(3, 7, 20))]
mu_ = mu_1 + mu_2 + mu_3 + mu_4
mu_c = cycle(mu_)

#create active figure using a loop
while True:

    #use __next__ method to retrieve next item (Gaussian mean) from cycle iterator
    mu = next(mu_c)

    #generate 2D Gaussian
    z = (1 / np.sqrt(2 * np.pi * sigma)) * np.exp(-((x_ - mu[0])**2 + (y_ - mu[1])**2) / (2 * sigma**2))

    #remove tick labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    #plot 2D Gaussian, pause for 0.01 seconds
    plt.imshow(z, cmap = 'inferno')
    plt.axis('off')
    plt.pause(0.01)
    ax.clear()