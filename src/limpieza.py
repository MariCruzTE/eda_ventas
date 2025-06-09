import pandas as pd
import numpy as np
import ast

def dollars_float(dataframe,col):
     dataframe[col] = dataframe[col].str.replace("$", "").astype(float)
     return dataframe


def extract_location(valor): # valor es el valor de una columna del dataframe
     try:
          split_data = valor.split("\n")
          address = split_data[0] if len(split_data) > 0 else np.nan
          city = " ".join(split_data[1].split()[:-1]) if len(split_data) > 1 else np.nan
          zip_code =split_data[1].split()[-1] if len(split_data) > 1 else np.nan
          if len (split_data) > 2:
               try:
                    latitude, longitude = ast.literal_eval(split_data[2])
               except(SyntaxError, ValueError, TypeError):
                    latitude, longitude = np.nan, np.nan
          else:
               latitude, longitude = np.nan, np.nan
          return pd.Series([address,
                         city,
                         zip_code,
                         latitude,
                         longitude])
     except(IndexError, ValueError):
          return pd.Series([np.nan,
                           np.nan,
                           np.nan,
                           np.nan,
                           np.nan])
          
          
def null_values(dataframe):
     count_null = dataframe.isnull().sum()
     percen_null = (count_null / dataframe.shape[0])
     df_null = pd.DataFrame({
          "Null Values": count_null,
          "Null percen": percen_null  
     })
     return df_null