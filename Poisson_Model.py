"""
Poisson Distribution Model
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def plot_poisson(lam=3):
    """
    Plot Poisson PMF
    """

    x = np.arange(0, 15)
    y = poisson.pmf(x, lam)

    plt.figure()
    plt.bar(x, y)
    plt.title(f"Poisson Distribution (λ={lam})")
    plt.xlabel("Events")
    plt.ylabel("Probability")
    plt.grid()
    plt.show()


def poisson_probability(lam, x):
    """
    Compute P(X = x)
    """
    return poisson.pmf(x, lam)


if __name__ == "__main__":
    plot_poisson()

    prob = poisson_probability(3, 5)
    print(f"P(X=5 | λ=3) = {prob:.4f}")