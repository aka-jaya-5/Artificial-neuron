import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def artificial_neuron(inputs, weights, bias):
    weighted_sum = np.dot(inputs, weights) + bias
    output = sigmoid(weighted_sum)
    return output

inputs = np.array([0.5, 0.3, 0.2])  # Inputs
weights = np.array([0.8, 0.4, 0.6])  # Weights
bias = 0.1  # Bias

output = artificial_neuron(inputs, weights, bias)

print(f"Output neuron: {output}")
Example Output:
