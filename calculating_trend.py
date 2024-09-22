import math

from utils import calculate_mean


class calculate_trend:

    def __init__(self,dataset:list[list[int]],point=(0,0)) -> None:
        
        self.dataset = dataset
        self.n = len(dataset[0])
        self.point = (calculate_mean(dataset[0]),calculate_mean(dataset[1]))
        
        ((Vx,Vy),covariance) = self.summation_of_x_minus_xbar()
        
        self.variance = (((Vx)/(self.n-1)),((Vy)/(self.n-1)))

        self.covariance = covariance/(self.n-1)

        self.correlation = (self.covariance)/(math.sqrt(self.variance[0]) * math.sqrt(self.variance[1]))

    def summation_of_x_minus_xbar(self):
        """
        Vx = ( x - xbar)
        """

        Vx, Vy,covariance = 0,0,0

        meanx,meany = self.point

        for numx,numy in zip(self.dataset[0],self.dataset[1]):
            nx = (numx - meanx)
            ny = (numy - meany)

            Vx += (nx**2)
            Vy += (ny**2)

            covariance += (nx*ny)


        return ((Vx,Vy),covariance)
    
    





if __name__ == "__main__":
    trend = calculate_trend(
        [
            [1,2,3,4,5],
            [1,2,3,4,5]
        ]
    ) 

    print(f"Variance={trend.variance}")
    print(f"Covariance={trend.covariance}")
    print(f"Correlation={trend.correlation}")
        