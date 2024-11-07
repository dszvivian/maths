import  matplotlib.pyplot as plt

from dataset_loader import DatasetLoader
from Animation import Animate 
from math import exp
from sigmoid import sigmoid


class LogisticRegression:
    
    def __init__(self) -> None:
        self.m = 0 
        self.b = 0
        self.X = None
        self.Y = None 

        self.animate = Animate()

    def train(self,
              X,Y,
              epochs=100,
              learning_rate = 0.001,
              animate=False
              ):
        
        self.X = X
        self.Y = Y

        for _ in range(epochs):
            self.m, self.b = self.gradient_descent(
                X,Y,
                self.m,
                self.b,
                learning_rate
            )
            

            if animate:
                self.animate.plot_each_frame(
                    X=self.X,
                    Y=self.Y,
                    m=self.m,
                    b=self.b,
                    pause_time_between_each_frame=1
                )

            print(f"m={self.m}  b={self.b}")

    def gradient_descent(
            self,
            X,Y,
            m=0,b=0,
            learning_rate=0.001
            ):
        
        n = len(X)
        gradient_m, gradient_b = 0,0

        for i in range(n):                    
            y_pred = sigmoid((m*X[i])+b)

            gradient_m =  (1/n) * (2*X[i]*(y_pred - Y[i]))
            gradient_b =  (1/n) * (2*(y_pred - Y[i]))

        final_m  = m - gradient_m * learning_rate
        final_b  = b - gradient_b * learning_rate

        return final_m, final_b           



        
    
    def plot(self,title="Best Fit Line"):
        plt.title(title)
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.scatter(self.X,self.Y)

        x_new = [min(self.X), max(self.X)]
        y_new = []

        for item in x_new:
            y_new.append(((self.m*item)+self.b))

        plt.plot(x_new,y_new)
        plt.show()

    def point_desicion_boundary():
        return NotImplementedError("Point Desicion Boundary")

    def predict(self, X):
      return sigmoid((self.m * X) + self.b)


if __name__ == "__main__":
    obese_not_obese_dataset = DatasetLoader()
    obese_not_obese_dataset.csv_to_array(path="./datasets/obesity-classification-dataset.csv")

    regressor = LogisticRegression()
    regressor.train(obese_not_obese_dataset.X,obese_not_obese_dataset.Y)
    print(f"Actual value = {obese_not_obese_dataset.Y[-1]} Predicted Value = {regressor.predict(obese_not_obese_dataset.X[-1])}")