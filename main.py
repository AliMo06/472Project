import math
import numpy as np
import matplotlib
from scipy.stats import norm
import pandas as pd

def BlackScholes():
    print("fix")

def MonteCarlo():
    print("Fix")

data = pd.read_csv("datasets/Mercedes_Stock.csv") #Pandas reading stock data

SO, ST, K, R, sigma, T, Z, N, VO = 0, 0, 0, 0, 0, 0, 0, 0, 0 #Declaration of variables

if __name__ == "__main__":
    option  = input("Enter the pricing you would like to calculate with \n1. Open \n2. Close \n3.Adjusted Close \n4. High \n5. Low").lower() #User input for option type



