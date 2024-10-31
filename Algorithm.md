## Genearal regression Algorithm:


- **Step1:** *Cost Function*
    - Using Cost Function You can manually draw any random Line  
    - And Calculate the Correctness of that Line  
    Using Cost Function

- **Step2:** Training Loop
        
    - Setting the Epochs(ie: Number of Time You want to run the Training Loop)  

    - Initialize the Weights and biases  
    (ie In case of Line Weight=slope and Biases=y-intercept)
    at Random Maybe 0
    
    - Under each Epoch  
        - We will Differentiate the Cost Function
        
        - By differentiating Cost Function wrt Weight 
            We will Get gradient_weight

        - By differentiating Cost Function wrt Biases  
            We will get gradient_bias

        We differentiate Inorder to Find the Direction towards Global Mininma(ie:A Point which has minimum Deviation from Best Fit Line)

   -  **Apply Convergence Theorem:**
    
        - Choose a Learning rate(How fast you want to Converge to Gloval Minima)
    based on the training size, you can choose learning_rate accordingly 

        - Caution: 
    Choosing a Very large Learning Rate will make your point to never Converge to Global minima 
    Choosing a Very small learning Rate will make your point too late to Converge to Global Minima  

        - Update Weights and biases:
    Multiply learning_rate with gradient_weight and Subtract it with Weight of last Iteration
    Multiply learning_rate with gradient_Bias and Subtract it with Bias of last Iteration



