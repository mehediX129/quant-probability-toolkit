"""
Gamma Function vs Factorial Comparison
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def plot_gamma_vs_factorial():
    """
    Compare Gamma function with factorial
    """

    x = np.linspace(1, 6, 100)
    y = [math.gamma(i) for i in x]

    # Integer points
    x_int = np.arange(1, 6)
    y_int = [math.factorial(i - 1) for i in x_int]

    plt.figure()
    plt.plot(x, y, label="Gamma Function")
    plt.scatter(x_int, y_int, label="Factorial Points")

    plt.title("Gamma vs Factorial")
    plt.xlabel("X")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    plot_gamma_vs_factorial()