import math
import numpy as np
import matplotlib
from scipy.stats import norm
import pandas as pd

def BlackScholes():
    print("Fix")

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
        results.append(S_TClosedForm(SO, R, sigma, T, Z))

    return np.mean(results)


data = pd.read_csv("datasets/Mercedes_Stock.csv") #Pandas reading stock data



if __name__ == "__main__":
    option  = input("Enter the pricing you would like to calculate with \n1. Open \n2. Close \n3.Adjusted Close \n4. High \n5. Low").lower() #User input for option type
    SO, ST, K, R, sigma, T, Z, N, VO = 0, 0, 0, 0, 0, 0, 0, 0, 0 #Declaration of variables


