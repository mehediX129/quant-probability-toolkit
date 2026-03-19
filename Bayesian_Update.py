"""
Bayesian Update using Beta Distribution
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


def plot_beta(prior_a=2, prior_b=2, post_a=10, post_b=5):
    """
    Plot prior and posterior distributions
    """

    x = np.linspace(0, 1, 500)

    prior = beta.pdf(x, prior_a, prior_b)
    posterior = beta.pdf(x, post_a, post_b)

    plt.figure()
    plt.plot(x, prior, label="Prior")
    plt.plot(x, posterior, label="Posterior")
    plt.title("Bayesian Update (Beta Distribution)")
    plt.xlabel("Probability")
    plt.ylabel("Density")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    plot_beta()