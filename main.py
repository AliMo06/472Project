import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

def BlackScholes(SO, K, R, sigma, T):
    # Calculate d1
    d1 = (np.log(SO/K) + (R + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))

    # Calculate d2
    d2 = d1 - sigma*np.sqrt(T)

    # Calculate call option price
    C = SO*norm.cdf(d1) - K*np.exp(-R*T)*norm.cdf(d2)

    return C

def S_TClosedForm(SO, R, sigma, T, Z):
    # Let the close form be expressed as ST = S_0 * e^(A + B)
    # (r - 1/2(sigma^2)) * T = A
    A = (R - ((1/2)*(sigma**2))) * T

    # sigma * sqrt(T) * Z = B
    B = sigma * math.sqrt(T) * Z

    # e ^ (A+B)
    eAB = np.exp((A + B))

    # S_0 * e^(a+b)
    return ((SO * eAB))

def MonteCarlo(SO, K, R, sigma, T, N):
    #Vectorized Monte Calro by initializing Z as a numpy array of random variables where Z ~ N(0,1)
    Z = np.random.normal(0, 1, N)

    ST = S_TClosedForm(SO, R, sigma, T, Z)

    payoff = np.maximum(ST - K, 0)
    discounted_payoff = np.exp(-R*T) * payoff
    price = np.mean(discounted_payoff)

    standard_error = np.std(discounted_payoff, ddof=1) / np.sqrt(N)
    lower = price - (1.96 * standard_error)
    upper = price + (1.96 * standard_error)

    return price, standard_error, lower, upper


def StockVolatility(prices):
    #R_t = ln(S_t/S_t-1)

    Rt = np.log(prices[1:] / prices[:-1])

    #sigma = std(R_t) * sqrt(252)
    sigma = np.std(Rt, ddof=1) * np.sqrt(252)

    return sigma

def MakePlots():
    print("fix")

if __name__ == "__main__":
    data = pd.read_csv("datasets/Mercedes_Stock.csv")

    option  = input("Enter the pricing you would like to calculate with \n1. Open \n2. Close \n3.Adjusted Close \n4. High \n5. Low").lower() #User input for option type
    
    #Based on Option
    if option == "1":
        prices = data["Open"].to_numpy()
    elif option == "2":
        prices = data["Close"].to_numpy()
    elif option == "3":
        prices = data["Adj Close"].to_numpy()
    elif option == "4":
        prices = data["High"].to_numpy()
    elif option == "5":
        prices = data["Low"].to_numpy()
    else:
        raise ValueError("Invalid selection")


    SO = 100
    K = 105
    R = 0.05
    sigma = 0.20
    T = 1
    N = 100000

    #Calculate Volatility
    sigma = StockVolatility(prices)

    #Black-Scholes
    VO = BlackScholes(SO, K, R, sigma, T)

    # Monte Carlo
    MC, SE, lower, upper = MonteCarlo(SO, K, R, sigma, T, N)
