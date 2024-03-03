import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    lin1 = linregress(x, y)

    plt.plot(np.arange(df['Year'].min(), 2051), np.arange(df['Year'].min(), 2051) * lin1.slope + lin1.intercept, color='red')

    # Create second line of best fit
    df_2 = df[df['Year'] >= 2000]
    x_2 = df_2['Year']
    y_2 = df_2['CSIRO Adjusted Sea Level']

    lin_2 = linregress(x_2, y_2)

    plt.plot(np.arange(2000, 2051), lin_2.intercept + lin_2.slope * np.arange(2000, 2051), color='blue')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()