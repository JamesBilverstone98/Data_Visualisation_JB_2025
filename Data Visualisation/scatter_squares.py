import matplotlib.pyplot as plt
# importing the pyplot module using plt as to not type pyplot constantly
# pyplot module contains a number of functions that help generate charts/plots

import seaborn as sns
# allows program to utilise the seaborn library 

# can pass scatter() separate lists of x and y values
x_values = range(1, 1001) # Python can plot 1000 points as easily as 5 points
y_values = [x**2 for x in x_values] # loops through the x_values and squares it

plt.style.use('seaborn-v0_8')
# seaborn is a default library in Matplotlib

fig, ax = plt.subplots() 
# fig represents the entire figure
# ax represents a single plot in the figure
ax.scatter(x_values, y_values, colour='red', s=10) 
# s argument to set the size of the dots, colour to change points colour
# to plot a single point, pass the single x and y values to the scatter method

# set the chart title and label axes
ax.set_title("Square Numbers", fontsize=24) # overall title of chart
ax.set_xlabel("Value", fontsize=14) # title of x label
ax.set_ylabel("Square of Value", fontsize=14) # title of y label

# set the range for each axis
ax.axis([0, 1100, 0, 1_100_000]) # the axis method requires 4 values
# the minimum and maximum values for the x and y axis 

# set the size of the tick labels
ax.tick_params(labelsize=14) # styles the tick marks

plt.show() # this opens Matplotlib's viewer and displays the plot