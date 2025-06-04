import numpy as np
from statistics import NormalDist

norm_cdf = NormalDist().cdf

class BSM_Model:


    def __init__(self, spot_price, strike_price, days_to_expiry, risk_free_rate, volatility):

        
        self.spot = spot_price
        self.strike = strike_price
        self.T = days_to_expiry / 365 
        self.r = risk_free_rate
        self.sigma = volatility
    #The function N(x) is the cumulative probability distribution function for a variable with
    # a standard normal distribution. In other words, it is the probability that a variable with
    # a standard normal distribution will be less than x
    # Cumulative distribution function for the standard normal distribution of the d1 value
    def d1(self): 
        return (np.log(self.spot / self.strike) + (self.r + self.sigma ** 2 / 2) * self.T) / (self.sigma * np.sqrt(self.T))
    # Cumulative distribution function for the standard normal distribution of the d2 value
    # Interpretation of N(d2) is a probability that the option will be exercised in a risk-neutral world
    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)
    
    def d1_dividend(self, dividend_yield):
        return (np.log(self.spot / self.strike) + (self.r - dividend_yield + self.sigma ** 2 / 2) * self.T) / (self.sigma * np.sqrt(self.T))
    
    def d2_dividend(self, dividend_yield):
        return self.d1_dividend(dividend_yield) - self.sigma * np.sqrt(self.T)
    



    def call_price(self):
        return (self.spot * norm_cdf(self.d1()) - self.strike * np.exp(-self.r * self.T) * norm_cdf(self.d2()))
    

    def put_price(self):
        return (self.strike * np.exp(-self.r * self.T) * norm_cdf(-self.d2()) - self.spot * norm_cdf(-self.d1()))
    

    def call_price_dividend(self, dividend_yield):
        adjusted_spot = self.spot * np.exp(-dividend_yield * self.T)
        return (adjusted_spot * norm_cdf(self.d1_dividend(dividend_yield)) - self.strike * np.exp(-self.r * self.T) * norm_cdf(self.d2_dividend(dividend_yield)))

    def put_price_dividend(self, dividend_yield):
        adjusted_spot = self.spot * np.exp(-dividend_yield * self.T)
        return (self.strike * np.exp(-self.r * self.T) * norm_cdf(-self.d2_dividend(dividend_yield)) - adjusted_spot * norm_cdf(-self.d1_dividend(dividend_yield)))

    





class Black_Model:
    def __init__(self, f_price, strike_price, days_to_expiry, risk_free_rate, volatility):
        self.f = f_price
        self.strike = strike_price
        self.T = days_to_expiry / 365
        self.r = risk_free_rate
        self.sigma = volatility

    def d1(self):
        return (np.log(self.f / self.strike) + (self.sigma ** 2 / 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)
    # c = e-rT[F0*N(d1) - KN(d2)] 
    def call_price(self):
        return (np.exp(-self.r * self.T) * (self.f * norm_cdf(self.d1()) - self.strike * norm_cdf(self.d2())))
    # p = e-rT[KN(-d2) - F0*N(-d1)]
    def put_price(self):
        return (np.exp(-self.r * self.T) * (self.strike * norm_cdf(-self.d2()) - self.f * norm_cdf(-self.d1())))





        






    





       
    




    




