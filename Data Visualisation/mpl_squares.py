import matplotlib.pyplot as plt
# importing the pyplot module using plt as to not type pyplot constantly
# pyplot module contains a number of functions that help generate charts/plots

import seaborn as sns
# allows program to utilise the seaborn library 

input_values = [1, 2, 3, 4, 5]
# input values for the squared numbers

squares = [1, 4, 9, 16, 25] 
# this will hold the data we will plot for the actual squared numbers

plt.style.use('seaborn-v0_8')
# seaborn is a default library in Matplotlib

fig, ax = plt.subplots() 
# fig represents the entire figure
# ax represents a single plot in the figure

ax.plot(input_values, squares, linewidth=3)
# the linewidth parameter controls the thickness of the line that plot generates

# set the chart title and label axes
ax.set_title("Square Numbers", fontsize=24) # overall title of chart
ax.set_xlabel("Value", fontsize=14) # title of x label
ax.set_ylabel("Square of Value", fontsize=14) # title of y label

# set the size of the tick labels
ax.tick_params(labelsize=14) # styles the tick marks

plt.show() # this opens Matplotlib's viewer and displays the plot
 
