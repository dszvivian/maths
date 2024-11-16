
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

    def derivation_of_cost_function_wrt_weight():
        raise NotImplementedError("Cost Function is Not Defined") 

    def derivation_of_cost_function_wrt_bias():
        raise NotImplementedError("Cost Function is Not Defined") 

    def update_weight_biases(
            self,
            weight,gradient_weight,
            bias,gradient_bias):
        weight =  weight - self.learning_rate * gradient_weight
        bias   =  bias   - self.learning_rate * gradient_bias

        return weight,bias
    
    def calculate_gradient(
            self
    ):        
        gradient_weight = 0
        gradient_bias = 0  

        for _ in range(self.n):
            gradient_weight += self.derivation_of_cost_function_wrt_weight()
            gradient_bias += self.derivation_of_cost_function_wrt_bias()

        return self.update_weight_biases(
            self.weight,gradient_weight,
            self.bias,gradient_bias
        )
        
    def train(self):
        
        for _ in range(self.epochs):
            self.weight, self.bias = self.calculate_gradient()
