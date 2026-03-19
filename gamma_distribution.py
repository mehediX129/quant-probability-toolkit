"""
Gamma Distribution Visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma


def plot_gamma():
    """
    Plot Gamma distribution for multiple shape values
    """

    x = np.linspace(0, 20, 500)

    plt.figure()
    for k in [1, 2, 5]:
        y = gamma.pdf(x, a=k)
        plt.plot(x, y, label=f"k={k}")

    plt.title("Gamma Distribution")
    plt.xlabel("X")
    plt.ylabel("Density")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    plot_gamma()