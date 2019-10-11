from matplotlib import pyplot as plt

#######################################################################

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis

plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y-axis

plt.ylabel("Billions of $")
plt.show()

#######################################################################

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x+y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance', marker='o') # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # re dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line

plt.legend(loc=9) # centered legend
plt.xlabel("mode complexity")
plt.xticks([])
plt.title("The bias-variance tradeoff")
plt.show()
