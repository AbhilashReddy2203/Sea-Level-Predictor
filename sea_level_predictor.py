# Sea-Level-Predictor
def draw_plot():
    # Load the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create the scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data')

    # Get the slope and y-intercept of the line of best fit for the entire dataset
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Predict the sea level rise in 2050 using the line of best fit for the entire dataset
    future_years = pd.Series(range(1880, 2051))
    plt.plot(future_years, intercept + slope * future_years, color='r', label='Line of Best Fit (1880-2050)')

    # Filter the data for years from 2000 to the most recent year
    df_recent = df[df['Year'] >= 2000]

    # Get the slope and y-intercept of the line of best fit for the recent data
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Predict the sea level rise in 2050 using the line of best fit for the recent data
    future_years_recent = pd.Series(range(2000, 2051))
    plt.plot(future_years_recent, intercept_recent + slope_recent * future_years_recent, color='g', label='Line of Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Add a legend
    plt.legend()

    # Save and return the plot
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
