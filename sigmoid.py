from dataset_loader import DatasetLoader
from math import exp


# what does Sigmoid function do to a array of values


def sigmoid(point):
    return (1/(1+exp(-point)))



if __name__ == "__main__":

    X = [i for i in range(10)]
    Y = [i for i in range(10)]

    normal_values = DatasetLoader(X=X,Y=Y)
    normal_values.visualize_dataset(title="Normal Values")

    Y = [sigmoid(i) for i in Y]

    sigmoid_values = DatasetLoader(X=X,Y=Y)
    sigmoid_values.visualize_dataset("Sigmoid Values")