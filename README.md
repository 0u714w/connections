This script generates a line plot of monthly connections from the years 2016 to 2024.

The data is structured in a dictionary where each key is a year and the value is another dictionary
mapping each month to the number of connections. Missing values are filled with None.

The script performs the following steps:
1. Imports the necessary library (matplotlib.pyplot).
2. Sets up the data in a nested dictionary format.
3. Prepares the data for plotting by extracting months and years.
4. Initializes the plot with a specified figure size.
5. Iterates over each year, extracts the number of connections for each month, and plots the data.
6. Customizes the plot with a title, axis labels, legend, rotated x-ticks, and a grid.
7. Adjusts the layout to fit all elements neatly.
8. Displays the plot.


Usage:
- `python3 plot.py`