import numpy as np
import matplotlib.pyplot as plt

def fourier_series_analysis(f, T, N, x_values):
    """
    Perform Fourier series analysis on a given function.

    :param f: The function to analyze (function handle).
    :param T: The period of the function.
    :param N: The number of Fourier coefficients to calculate.
    :param x_values: The x values to evaluate.
    :return: The reconstructed function values at x_values.
    """
    a0 = (2 / T) * np.trapz([f(x) for x in np.linspace(-T/2, T/2, 1000)], dx=T/1000)
    fourier_sum = a0 / 2

    for n in range(1, N + 1):
        an = (2 / T) * np.trapz([f(x) * np.cos(2 * np.pi * n * x / T) for x in np.linspace(-T/2, T/2, 1000)], dx=T/1000)
        bn = (2 / T) * np.trapz([f(x) * np.sin(2 * np.pi * n * x / T) for x in np.linspace(-T/2, T/2, 1000)], dx=T/1000)
        
        fourier_sum += an * np.cos(2 * np.pi * n * x_values / T) + bn * np.sin(2 * np.pi * n * x_values / T)

    return fourier_sum

# Define the function to analyze
def target_function(x):
    return np.sin(x) + 0.5 * np.sin(2 * x)

# Parameters
T = 2 * np.pi  # Period of the function
N = 10  # Number of Fourier coefficients
x_values = np.linspace(-T, T, 1000)  # Range of x values

# Perform Fourier series analysis
reconstructed_function = fourier_series_analysis(target_function, T, N, x_values)

# Plot the original and reconstructed functions
plt.figure(figsize=(12, 6))
plt.plot(x_values, target_function(x_values), label='Original Function', linewidth=2)
plt.plot(x_values, reconstructed_function, label='Reconstructed Function', linestyle='--', linewidth=2)
plt.legend()
plt.title('Fourier Series Analysis')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()