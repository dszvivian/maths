import pandas as pd
import matplotlib.pyplot as plt

class DatasetLoader:

    def __init__(self,X=None,Y=None) -> list:
        self.dataset = None  
        self.X = X
        self.Y = Y    

    def csv_to_array(self,path):
        """"
        Converts csv file to and returns 
        Two arrays of X and Y
        """
        self.dataset = pd.read_csv(path)
        X = self.dataset.iloc[:,0].tolist()
        Y = self.dataset.iloc[:,1].tolist()

        self.X = X
        self.Y = Y

        return X, Y  
    
    def visualize_dataset(self,title="Visualizing Dataset"):
        plt.title(title)

        plt.axis('equal')
        plt.xlim(min(self.X),max(self.X))
        plt.ylim(min(self.Y),max(self.Y))

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.scatter(self.X,self.Y)

        plt.show()


if __name__ == "__main__":
    pass


        