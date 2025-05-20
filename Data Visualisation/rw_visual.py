import matplotlib.pyplot as plt
# importing the pyplot module using plt as to not type pyplot constantly
# pyplot module contains a number of functions that help generate charts/plots

from random_walk import RandomWalk
# this imports the RandomWalk class from the file

# keep making new walks as long as the program is active
while True:
    # make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(14, 5)) # sets the size of the figure
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    ax.set_aspect('equal')
    # by default matplotlib scales each axis independently, the set_aspect method
    # ensures both axes have equal spacing between the tick marks
    
    # emphasise the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
             s=100)
    
    # remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Another walk plotted? (y/n) ")
    if keep_running == 'n':
        break # if user input is no, exit program