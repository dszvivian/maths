import matplotlib.pyplot as plt
from Animation import Animate

from dataset_loader import DatasetLoader

class LinearRegression:

    def __init__(self) -> None:
        self.m = -10 
        self.b = -10
        self.X = None
        self.Y = None 

        self.animate = Animate()

    def train(self,
              X,Y,
              epochs=1000,
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
                    pause_time_between_each_frame=0.001
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

            gradient_m += -(2/n) * X[i] * (Y[i] - ((m * X[i]) + b))
            gradient_b += -(2/n) * (Y[i] - ((m * X[i]) + b))        

        final_m = m - gradient_m * learning_rate
        final_b = b - gradient_b * learning_rate

        return final_m,final_b
    
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
        
    def predict(self, X):
      return (self.m * X) + self.b
         
        


if __name__ == "__main__":

    X,Y = DatasetLoader().csv_to_array("./datasets/Salary_dataset.csv")

    regressor = LinearRegression()
    regressor.train(X[:-1],Y[:-1],animate=True)
    regressor.plot()
    print(f"Actual value = {Y[-1]} Predicted Value = {regressor.predict(X[-1])}")