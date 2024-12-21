import matplotlib.pyplot as plt


# Data setup
data = {
    year: {month: value for month, value in zip(
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        values
    ) if value is not None} for year, values in {
        2016: [None, None, None, None, None, None, None, 8, 7, 15, 7, 13],
        2017: [15, 17, 10, 18, 12, 13, 10, 16, 15, 20, 17, 5],
        2018: [20, 19, 18, 11, 23, 11, 13, 22, 8, 12, 14, 8],
        2019: [17, 35, 18, 28, 32, 26, 11, 20, 11, 20, 13, 17],
        2020: [22, 21, 17, 26, 19, 14, 15, 9, 10, 15, 7, 7],
        2021: [8, 8, 10, 12, 10, 13, 7, 13, 14, 8, 13, 11],
        2022: [16, 8, 10, 12, 10, 5, 14, 16, 25, 9, 10, 11],
        2023: [16, 7, 17, 21, 10, 11, 11, 25, 26, 16, 13, 33],
        2024: [31, 29, 25, 36, 33, 41, 12, 25, 24, 21, 51, 12],
    }.items()
}

# Prepare data for plotting
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
years = list(data.keys())

# Initialize plot
plt.figure(figsize=(14, 8))

for year in years:
    connections = [data[year].get(month, 0) for month in months]  # Fill missing months with 0
    plt.plot(months, connections, marker='o', label=str(year))

# Customize the plot
plt.title('Monthly Connections from 2016 to 2024')
plt.xlabel('Month')
plt.ylabel('Number of Connections')
plt.legend(title='Year')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()