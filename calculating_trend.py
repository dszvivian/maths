from utils import calculate_mean


class calculate_trend:

    def __init__(self,dataset:list[list[int]],point=(0,0)) -> None:
        
        self.dataset = dataset
        self.R = self.correlation()
        self.n = len(dataset[0])
        self.point = (calculate_mean(dataset[0]),calculate_mean(dataset[1]))

        print(self.point)
        
        


    def correlation(self):
        pass


    def variance(dataset,mean):
        """
        calcultes sum of all variance of all points 
        returns (x,y)
        """

        pass

    

    







if __name__ == "__main__":
    calculate_trend(
        [
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5]
        ]
    ) 
        