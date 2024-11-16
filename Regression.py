from GradientDescent import GradientDescent


class Regression(GradientDescent):

    def __init__(self,
                dataset,
                learning_rate,epochs,
                initial_weight, initial_bias):
        super().__init__(dataset,
              learning_rate,epochs,
              initial_weight,initial_bias)

    def cost_function():
        raise NotImplementedError("Cost Function is Not Defined")
    
    def derivation_of_cost_function_wrt_weight(n,X,Y,weight,bias):
        raise NotImplementedError("Cost Function is Not Defined") 

    def derivation_of_cost_function_wrt_weight(n,X,Y,weight,bias):
        raise NotImplementedError("Cost Function is Not Defined")     
        
          




    



