# Artificial Neuron Implementation

This project implements a simple artificial neuron using Python and NumPy. The neuron uses the sigmoid activation function to compute its output based on given inputs, weights, and a bias.

Follow me:
- Instagram: [programmer.pedia](https://www.instagram.com/programmer.pedia)
- YouTube: [Programmer Pedia](https://www.youtube.com/c/ProgrammerPedia)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

## Features

- Simple implementation of an artificial neuron.
- Uses the sigmoid activation function.
- Demonstrates how inputs, weights, and bias contribute to the output.

## Code Explanation

1. **Sigmoid Function**: This function takes a real-valued input and squashes it to a range between 0 and 1.
    ```python
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    ```

2. **Artificial Neuron Function**: This function computes the weighted sum of inputs, adds a bias, and applies the sigmoid function to obtain the output.
    ```python
    def artificial_neuron(inputs, weights, bias):
        weighted_sum = np.dot(inputs, weights) + bias
        output = sigmoid(weighted_sum)
        return output
    ```

3. **Inputs, Weights, and Bias**: Sample inputs, weights, and bias values are defined to test the neuron.
    ```python
    inputs = np.array([0.5, 0.3, 0.2])  # Inputs
    weights = np.array([0.8, 0.4, 0.6])  # Weights
    bias = 0.1  # Bias
    ```

4. **Output**: The output of the neuron is printed to the console.
    ```python
    output = artificial_neuron(inputs, weights, bias)
    print(f"Output neuron: {output}")
    ```

## Requirements

- Python 3.x
- NumPy library

You can install NumPy using pip:

```bash
pip install numpy
