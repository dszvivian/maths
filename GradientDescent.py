
class GradientDescent:

    def __init__(self,dataset):
        self.weight = 0
        self.bias = 0 

        self.X, self.Y = dataset 
        self.n = len(self.X)

    def derivation_of_cost_function_wrt_weight():
        pass 

    def derivation_of_cost_function_wrt_bias():
        pass 

    def update_weight_biases(
        weight,gradient_weight,
        bias,gradient_bias,
        learning_rate =  0.0001
    ):
        weight =  weight - learning_rate * gradient_weight
        bias   =  bias   - learning_rate * gradient_bias

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
        
    def train(
            self,
            epochs
    ):
        
        for _ in range(epochs):
            self.weight, self.bias = self.calculate_gradient()
