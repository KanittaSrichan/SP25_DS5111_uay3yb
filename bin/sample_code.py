"""
DOCSTRING MODULE
"""

import matplotlib.pyplot as plt  # Importing matplotlib for plotting

def plot_regression_line(x, y, b):
    """
    This function plots the actual data points and the regression line.

    Parameters:
    x (list): Independent variable values.
    y (list): Dependent variable values.
    b (list): Coefficients for the regression line, where b[0] is the intercept
              and b[1] is the slope.
    """
    # Plotting the actual points as a scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)

    # Predicted response vector
    y_pred = b[0] + b[1]*x

    # Plotting the regression line
    plt.plot(x, y_pred, color="g")

    # Adding labels
    plt.xlabel('x')
    plt.ylabel('y')

    # Display the plot
    plt.show()
