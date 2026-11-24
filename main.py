import math
import numpy as np
import matplotlib
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
    A = (R - ((1/2)*(sigma))) * T

    # sigma * sqrt(T) * Z = B
    B = sigma * math.sqrt(T) * Z

    # e ^ (A+B)
    eAB = np.exp((A + B))

    # S_0 * e^(a+b)
    return ((SO * eAB))

def MonteCarlo(numSims):
    #Results array to hold results of simulation
    results = np.array([])
    
    for i in range(numSims):
        Z = np.random.normal() 
        results.append(S_TClosedForm(SO, R, sigma, T, Z))

    return np.mean(results)


data = pd.read_csv("datasets/Mercedes_Stock.csv") #Pandas reading stock data



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

    
    SO, ST, K, R, sigma, T, Z, N, VO = 0, 0, 0, 0, 0, 0, 0, 0, 0 #Declaration of variables

    # Example parameters
    SO = 100
    K = 105
    R = 0.05
    sigma = 0.20
    T = 1
    N = 100000

    # Black-Scholes
    VO = BlackScholes(SO, K, R, sigma, T)

    # Monte Carlo
    MC = MonteCarlo(N)

    print("Black-Scholes Price:", VO)
    print("Monte Carlo Expected Stock Price:", MC)
