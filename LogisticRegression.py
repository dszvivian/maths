import  matplotlib.pyplot as plt

from Regression import Regression

from dataset_loader import DatasetLoader
from activation_functions import sigmoid


class LogisticRegression(Regression):
    
    def __init__(self,
                dataset,
                learning_rate=0.001,epochs=1000,
                initial_weight=0,initial_bias=0
                ):
        
        super().__init__(dataset,
            learning_rate,epochs,
            initial_weight,initial_bias)
        
    def cost_function():
        pass

    def derivation_of_cost_function_wrt_weight(
          self,n,X,Y,weight,bias):
        y_norm = sigmoid((weight*X)+bias)
        return (1/n) * (2*X * (y_norm - Y))

    def derivation_of_cost_function_wrt_bias(
             self,n,X,Y,weight,bias):
        y_norm = sigmoid((weight*X)+bias) 
        return (1/n) * (2 * (y_norm - Y))        
    
    def point_desicion_boundary():
        return NotImplementedError("Point Desicion Boundary")

    def predict(self, X):
      return sigmoid((self.m * X) + self.b)


if __name__ == "__main__":
    dataset = DatasetLoader().csv_to_array(path="./datasets/obesity-classification-dataset.csv")
    regressor = LogisticRegression(dataset,epochs=10)
    regressor.train(animate=True)