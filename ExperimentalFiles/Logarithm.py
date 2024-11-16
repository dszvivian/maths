from math import log
import matplotlib.pyplot as plt

# Plotting graph to visualize, Logarithm


if __name__ == "__main__":
    
    x = [i for i in range(1,100)]
    y = [i for i in range(1,100)]

    logy = [ log(i) for i in y ]

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.axis('equal')

    negative_log = [ -log(i) for i in y]

    plt.plot(x,y)
    plt.plot(x,logy)
    plt.plot(x,negative_log)


    plt.show()
    




