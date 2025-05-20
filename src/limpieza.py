import pandas as pd
import numpy as np

def dollars_float(dataframe,col):
     dataframe[col] = dataframe[col].str.replace("$", "").astype(float)
     return dataframe