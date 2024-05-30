from matrix import *
from img import *
from activations import *
from operations import *
import os
class NeuralNetwork:
    def __init__(self, inputt, hidden, output, lr):
        self.inputt = inputt
        self.hidden = hidden
        self.output = output
        self.lr = lr
        self.hidden_weights = Matrix(hidden, inputt)
        self.output_weights = Matrix(output, hidden)
        self.hidden_weights.Randomize(hidden)
        self.output_weights.Randomize(output)

    def train(self, inputt: Matrix, output: Matrix):
        # Feed forward
        hidden_inputs = matrixDot(self.hidden_weights, inputt)
        hidden_outputs = matrixApply(sigmoid, hidden_inputs)
        final_inputs = matrixDot(self.output_weights, hidden_outputs)
        final_outputs = matrixApply(sigmoid, final_inputs)

        # Find errors
        output_errors = matrixSubtract(output, final_outputs)
        hidden_errors = matrixDot(matrixTranspose(self.output_weights), output_errors)

        # Backpropagate
        self.output_weights = matrixAdd(
            self.output_weights,
            matrixScale(
                self.lr,
                matrixDot(
                    matrixMultiply(output_errors, matrixApply(sigmoidPrime, final_outputs)),
                    matrixTranspose(hidden_outputs)
                )
            )
        )

        self.hidden_weights = matrixAdd(
            self.hidden_weights,
            matrixScale(
                self.lr,
                matrixDot(
                    matrixMultiply(hidden_errors, matrixApply(sigmoidPrime, hidden_outputs)),
                    matrixTranspose(inputt)
                )
            )
        )

    def predict(self, inputt: Matrix):
        hidden_inputs = matrixDot(self.hidden_weights, inputt)
        hidden_outputs = matrixApply(sigmoid, hidden_inputs)
        final_inputs = matrixDot(self.output_weights, hidden_outputs)
        final_outputs = matrixApply(sigmoid, final_inputs)
        return matrixApply(softmax, final_outputs)

    def save(self, file_string: str):
        import os
        os.makedirs(file_string, exist_ok=True)
        with open(os.path.join(file_string, "descriptor"), "w") as descriptor:
            descriptor.write(f"{self.inputt}\n{self.hidden}\n{self.output}\n")
        self.hidden_weights.save(os.path.join(file_string, "hidden"))
        self.output_weights.save(os.path.join(file_string, "output"))

    @staticmethod
    def load(file_string: str):
        with open(os.path.join(file_string, "descriptor"), "r") as descriptor:
            inputt = int(descriptor.readline().strip())
            hidden = int(descriptor.readline().strip())
            output = int(descriptor.readline().strip())
        hidden_weights = Matrix.load(os.path.join(file_string, "hidden"))
        output_weights = Matrix.load(os.path.join(file_string, "output"))
        lr = 0.1  # Set a default learning rate, or load it if saved
        net = NeuralNetwork(inputt, hidden, output, lr)
        net.hidden_weights = hidden_weights
        net.output_weights = output_weights
        return net

    def train_batch(self, imgs: list, batch_size: int):
        for i, img in enumerate(imgs[:batch_size]):
            if i % 100 == 0:
                print(f"Img No. {i}")
            img_data = img.img_data.flatten(0)  # Assuming img has a method to flatten it to a column vector
            output = Matrix(10, 1)
            output[img.label][0] = 1  # Setting the correct label
            self.train(img_data, output)

    def predict_img(self, img):
        img_data = img.img_data.flatten(0)  # Assuming img has a method to flatten it to a column vector
        return self.predict(img_data)

    def predict_imgs(self, imgs: list):
        n_correct = 0
        for img in imgs:
            prediction = self.predict_img(img)
            if prediction.Argmax() == img.label:
                n_correct += 1
        return n_correct / len(imgs)
