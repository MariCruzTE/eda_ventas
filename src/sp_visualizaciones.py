import numpy as np 
import pandas as pydll 
import matplotlib.pyplot as plt   
import seaborn as sns  

def visualizaciones(df):
     """
     Aplica visualizaciones exploratorias para variables categóricas y numéricas de un DataFrame.
          - Detecta y separa automáticamente las columnas categóricas (tipo object) y numéricas.
          - Genera gráficos de barras para las categóricas (`vis_categoricas`).
          - Genera histogramas y boxplots para las numéricas (`vis_numericas`).

     Args:
          df : pandas.DataFrame
          DataFrame completo que contiene tanto variables categóricas como numéricas. 
          
     Returns:
          None
          Muestra las visualizaciones en pantalla sin devolver  ningun objeto.
     """

     df_cat = df.select_dtypes(include='O')
     df_num = df.select_dtypes(include=np.number)
     
     vis_categoricas(df_cat)
     frecuencia_valores(df_cat)
     vis_numericas(df_num)
     
     
def frecuencia_valores(df):
     for col in df.columns:
          print(f'{col.upper()}')
          display(df[col].value_counts()/df.shape[0]*100)
          print('_________________________')



def vis_categoricas(df):
     """
     Genera visualizaciones de barras (countplots)
     para variables categóricas de un DataFrame.
     
     Cada variable del DataFrame se representa en una subgráfica individual dentro de una misma figura, 
     permitiendo analizar la distribución de frecuencias de cada categoría.

     Args:
         df (pandas.DataFrame): DataFrame que contiene únicamente columnas categóricas. Cada columna se representará en un gráfico de barras.
         
     Returns:
          None
          Muestra los gráficos en pantalla pero no devuelve ningun objeto
     """
     num_rows = len(df.columns)
     fig, axes = plt.subplots(num_rows,1, figsize= (14,20))

     #axes = axes.flatten()
     
     for i,col in enumerate(df.columns):
          sns.countplot(data=df, x=col, palette='mako', hue=col, ax=axes[i])
          axes[i].set_title(f"Barplot de {col}")
          axes[i].set_ylabel(f'Frecuencia')
          axes[i].set_xlabel('')
          axes[i].tick_params(axis = 'x', rotation = 90)
          
          
          
def vis_numericas(df):  
     """
     Genera visualizaciones para variables numéricas: histogramas y boxplots.

     Cada columna del DataFrame se representa mediante dos subgráficas:
    - Histograma para visualizar la distribución de frecuencias.
    - Boxplot para detectar la dispersión y posibles outliers.
    
     Args:
         df (pandas.DataFrame): DataFrame que contiene únicamente columnas numéricas. Cada columna se representará en dos tipos de gráfico.
         
     Returns:
          None
          Muestra los gráficos en pantalla pero no devuelve ninguún objeto.

     """
     num_rows = len(df.columns)     
     fig, axes = plt.subplots(num_rows, 2, figsize=(14, 60))

     for i, col in enumerate(df.columns):
          sns.histplot(data=df, x=col, ax=axes[i,0])
          axes[i, 0].set_title(f"Hisplot de {col}")
          axes[i, 0].set_ylabel(f'Frecuencia')
          axes[i, 0].set_xlabel('')
          
          sns.boxplot(data=df, x=col, ax=axes[i,1])
          axes[i, 1].set_title(f"Boxplot de {col}")
          axes[i, 1].set_xlabel('')
    
