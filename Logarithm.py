from math import log
import matplotlib.pyplot as plt


from dataset_loader import DatasetLoader













if __name__ == "__main__":
    
    x = [i for i in range(1,100)]
    y = [i for i in range(1,100)]


    normal_dataset = DatasetLoader(X=x, Y=y)
    normal_dataset.visualize_dataset(title="Normal Dataset")

    y = [ log(i) for i in y ]

    logarithmic_dataset = DatasetLoader(X=x, Y=y)
    logarithmic_dataset.visualize_dataset(title="Logarithmic Dataset")




