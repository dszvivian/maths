from math import log

# todo: come up with a better name that genrallizes this class
class Likelihood:

    def __init__(self,data=None,wins=0,failures=0):
        """
        data should be in binary form
        since we are calculating probability of Win or Failure
        """
        if data != None:        
            self.data = data

            self.wins = sum(1 for i in data if i==1)
            self.failures = len(data) - self.wins  
        else:
            self.wins = wins
            self.failures = failures     

    def probability(self):        
        return (self.wins/(self.wins+self.failures))
    
    def odds(self):
        return (self.wins/self.failures)
    
    def log_odds(self):
        return log(self.odds())
    
    def print_likelihood_stats(self):
        print(f"Probability(Wins) ={self.probability()}")
        print(f"Odds = {self.odds()}")
        print(f"Log Odds:{self.log_odds()}")
    
if __name__ == "__main__":

    print("--------------------------")
    print("If failures are high")
    wins = 1 
    failures = 4
    Likelihood(wins=wins, failures=failures).print_likelihood_stats()
    print("--------------------------")

    print("--------------------------")
    print("If failures are Too high")
    wins = 1 
    failures = 32
    Likelihood(wins=wins, failures=failures).print_likelihood_stats()
    print("--------------------------")

    print("--------------------------")
    print("If Wins are high")
    wins = 4
    failures = 1
    Likelihood(wins=wins, failures=failures).print_likelihood_stats()
    print("--------------------------")

    print("--------------------------")
    print("If Wins are Too high")
    wins = 32
    failures = 1
    Likelihood(wins=wins, failures=failures).print_likelihood_stats()
    print("--------------------------")




    