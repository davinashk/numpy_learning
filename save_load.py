import numpy as np

vector1=np.genfromtxt("data.csv",
                    delimiter=",",
                    dtype=float,
                    missing_values=["","nan"],
                    filling_values=np.nan)

print(vector1)