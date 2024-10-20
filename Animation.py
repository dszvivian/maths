import matplotlib.pyplot as plt

class Animate:
    
    def __init__(self):
        pass

    def plot_each_frame(
        self,
        X, Y,
        m, b,
        pause_time_between_each_frame=0.1
    ):
        """
        Need to call this method on Each Training Step
        to get Animation
        """
        plt.clf()

        plt.scatter(X,Y)

        x_new = [min(X), max(X)]
        y_new = []

        for item in x_new:
            y_new.append(((m*item)+b))

        plt.plot(x_new,y_new)
        plt.pause(pause_time_between_each_frame)
        
         
        


if __name__ == "__main__":
    pass