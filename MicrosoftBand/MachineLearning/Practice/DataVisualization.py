from __future__ import division, print_function
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 7))
# Font size to 14
matplotlib.rc('font', size = 14)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')
# In a notebook environment, display the plots inline
# %matplotlib inline



daily_path = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/SensorDatatestsample4.txt'
# daily_path = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/newSensorDatatest.txt'
daily_data = pd.read_csv(daily_path ,index_col=None, na_values=['NA'], usecols=['Gx'])


# Define a function for a plot with two y axes
def lineplot2y(x_data, x_label, y1_data, y1_color, y1_label):
    # Each variable will actually have its own plot object but they
    # will be displayed in just one plot
    # Create the first plot object and draw the line
    _, ax1 = plt.subplots()
    ax1.plot(x_data, y1_data, color = y1_color)
    # Label axes
    ax1.set_ylabel(y1_label, color = y1_color)
    ax1.set_xlabel(x_label)
    # ax1.set_title(title)

    # Create the second plot object, telling matplotlib that the two
    # objects have the same x-axis

    # ax2 = ax1.twinx()
    # ax2.plot(x_data, y2_data, color = y2_color)
    # ax2.set_ylabel(y2_label, color = y2_color)

    # Show right frame line
    # ax2.spines['right'].set_visible(True)
    plt.show()

# Call the function to create plot
lineplot2y(x_data = np.arange(1, 201, 1)
           , x_label = 'Time'
           , y1_data = daily_data
           , y1_color = '#539caf'
           , y1_label = 'Gx')
           # , y2_data = daily_data['Ay']
           # , y2_color = '#7663b0'
           # , y2_label = 'Ay'
           # , title = 'Accelerometer z-axis')
