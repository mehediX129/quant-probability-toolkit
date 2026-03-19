"""
Normal Distribution Visualization & Probability Tool
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def plot_normal_distribution(mean=0, std_dev=1):
    """
    Plot normal distribution with given mean and std deviation
    """

    # Generate data range
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 500)
    y = norm.pdf(x, mean, std_dev)

    plt.figure()
    plt.plot(x, y, label=f"N({mean}, {std_dev}^2)")
    plt.title("Normal Distribution")
    plt.xlabel("X")
    plt.ylabel("Density")
    plt.legend()
    plt.grid()
    plt.show()


def calculate_probability(z):
    """
    Calculate P(Z < z)
    """
    return norm.cdf(z)


if __name__ == "__main__":
    plot_normal_distribution()

    prob = calculate_probability(1)
    print(f"P(Z < 1) = {prob:.4f}")