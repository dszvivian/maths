import pandas as pd
import matplotlib.pyplot as plt

class DatasetLoader:

    def __init__(self,X=None,Y=None) -> list:
        self.dataset = None  
        self.X = X
        self.Y = Y


    #todo: Check wheather given list mathches with given value n 
    def validate_dataset(
            self,
            n=2
            ):
        """
        validates if it's a 2d array or not
        """
        return True
    

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
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.scatter(self.X,self.Y)

        plt.show()


if __name__ == "__main__":
    salary_dataset = DatasetLoader()

    print(salary_dataset.csv_to_array("./datasets/Salary_dataset.csv"))


        