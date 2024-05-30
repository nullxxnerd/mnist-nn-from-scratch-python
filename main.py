import time
import random
from matrix import *
from img import *
from activations import *
from operations import *
from nn import NeuralNetwork  # Assuming the class is in a module named neural_network

def main():
    random.seed(time.time())

    # # TRAINING
    # number_imgs = 10000
    # imgs = csv_to_imgs("./data/mnist_train.csv", number_imgs)
    # net = NeuralNetwork(784, 300, 10, 0.1)
    # net.train_batch(imgs, number_imgs)
    # net.save("testing_net")

    # PREDICTING
    number_imgs = 3000
    imgs = csv_to_imgs("data/mnist_test.csv", number_imgs)
    net = NeuralNetwork.load("testing_net")
    score = net.predict_imgs(imgs[:1000])
    print(f"Score: {score:.5f}")


if __name__ == "__main__":
    main()
