import matplotlib.pyplot as plt

from Animation import Animate
from dataset_loader import DatasetLoader
from Regression import Regression

class LinearRegression(Regression):

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
        return -(2/n) * X * (Y - ((weight * X)+bias)) 

    def derivation_of_cost_function_wrt_bias(
             self,n,X,Y,weight,bias):
        return -(2/n) * (Y - ((weight*X)+bias))
        
    def predict(self, X):
      return (self.m * X) + self.b
         
        


if __name__ == "__main__":
    dataset = DatasetLoader().csv_to_array("./datasets/Salary_dataset.csv")
    regressor = LinearRegression(dataset,epochs=10)
    regressor.train(animate=True)