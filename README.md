# Simple Neural Network from Scratch (without using PyTorch)

This project demonstrates how to build a neural network from scratch without using any deep learning libraries such as PyTorch or TensorFlow. 
The primary goal is educational: to help people understand the inner workings of neural networks by implementing them manually.

## Introduction
Neural networks are the backbone of many modern machine learning applications. However, the complexity of these frameworks can often obscure the fundamental principles behind how neural networks operate. This project aims to demystify neural networks by building a simple neural network from scratch, training it on the MNIST dataset, and explaining each step in detail.


## Dataset
The MNIST dataset, a collection of 70,000 handwritten digits, is used for training and evaluating the neural network. It contains 60,000 training images and 10,000 testing images. Each image is 28x28 pixels and labeled with the corresponding digit (0-9).
you can download the dataset from kaggle.

## Network Architecture
The neural network implemented in this project consists of the following:
- Input Layer: 784 neurons (28x28 pixels flattened)
- Hidden Layer: 128 neurons with ReLU activation
- Output Layer: 10 neurons with softmax activation

## Installation
To run the code in this repository, you need Python installed on your system. Follow these steps to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Ensure you have the necessary packages. Although no deep learning libraries are used, you may need basic packages like numpy matrix operations( if you want to speed things up rewrite the matrix operations using numpy).

    ```bash
    pip install numpy 
    ```

## Usage
Run the main script to train the neural network and evaluate its performance on the MNIST dataset.

```bash
python main.py
