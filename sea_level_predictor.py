import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    # Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv")

    # Create scatter plot
        # Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='CSIRO Sea Level')

    plt.title('Scatter Plot of Sea Level Over Time')
    plt.xlabel('Year')
    plt.ylabel('Sea Level')


    # Create first line of best fit
        # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
        # Plot the line of best fit over the top of the scatter plot. 
        # Make the line go through the year 2050 to predict the sea level rise in 2050.
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_values = pd.Series(df['Year'].tolist() + [2050])
    
    y_values = slope * x_values + intercept

    plt.plot(x_values, y_values, color='red', linestyle='--', label='Line of Best Fit')

    

    # Create second line of best fit
        # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. 
        # Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    df_second = df[(df['Year'] >= 2000) & (df['Year'] <= 2013)]

    slope_filtered, intercept_filtered, _, _, _ = linregress(df_second['Year'], df_second['CSIRO Adjusted Sea Level'])

    x_values_filtered = pd.Series(df_second['Year'].tolist() + [2050])

    y_values_filtered = slope_filtered * x_values_filtered + intercept_filtered

    plt.plot(x_values_filtered, y_values_filtered, color='yellow', linestyle='--', label='Line of Best Fit (2000-2013)')

    # Add labels and title
        # The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    plt.title('Sea Level Rise')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()