from Animation import Animate

class GradientDescent:

    def __init__(self,
                 dataset,
                 learning_rate,epochs,
                 initial_weight, initial_bias):
        self.weight = initial_weight
        self.bias = initial_bias

        self.learning_rate = learning_rate
        self.epochs = epochs

        self.X, self.Y = dataset 
        self.n = len(self.X)

        self.animate = Animate()

    def derivation_of_cost_function_wrt_weight(n,X,Y,weight,bias):
        raise NotImplementedError("Cost Function is Not Defined") 

    def derivation_of_cost_function_wrt_bias(n,X,Y,weight,bias):
        raise NotImplementedError("Cost Function is Not Defined") 

    def update_weight_biases(
            self,
            weight,gradient_weight,
            bias,gradient_bias):
        weight =  weight - self.learning_rate * gradient_weight
        bias   =  bias   - self.learning_rate * gradient_bias

        return weight,bias
    
    def calculate_gradient(self):        
        gradient_weight = 0
        gradient_bias = 0  

        for i in range(self.n):
            gradient_weight += self.derivation_of_cost_function_wrt_weight(
                self.n,
                self.X[i],
                self.Y[i],
                self.weight,
                self.bias
            )
            gradient_bias += self.derivation_of_cost_function_wrt_bias(
                self.n,
                self.X[i],
                self.Y[i],
                self.weight,
                self.bias
            )

        return self.update_weight_biases(
            self.weight,gradient_weight,
            self.bias,gradient_bias
        )
        
    def train(self,animate=False):
        
        for _ in range(self.epochs):
            self.weight, self.bias = self.calculate_gradient()

            if animate:
                self.animate.plot_each_frame(
                    self.X,self.Y,
                    self.weight,self.bias
                )
