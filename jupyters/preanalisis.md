# Preanalisis de los datos

- `date`, cambiar a formato fecha
- `store_name`, limpiar, algunos datos finalizan en  "/Spirit Lak"
- `store_location` necesita descomposicion en nuevas columnas, esta en mayusculas
- `category`, deberia ser category_number y pasar de float a int , hay valores Nan y **no se puede cambiar el tipo de datos antes del tratamiento de nulos**
- `county_number` , pasar de float a int, hay valores Nan y **no se puede cambiar el tipo de datos antes del tratamiento de nulos**
- `vendor_number`, pasar de float a int
- `state_bottle_cost`, de object a float, eliminar $
- `state_bottle_retail`,de object a float, eliminar $
- `sale(dollars)`,de object a float, eliminar $

## Normalizacion de datos

- tenemos dos columnas que miden el volumen en distintas unidades,('`bottle_volume(ml)` y `volume_sold(gallons)` ') hay que unificar a una misma unidad
galon = 3785.41 ml

## Transformación de Nulos

- `county_number` y `county`  
  - los nulos perteneen a registros de las ciudades ['GUTTENBERG', 'BELMOND']
  - buscar el county correspondiente y reemplazar null por los valores adecuados
    - clayton existe, county number 22
    - Wright tambien existe,county number 99

- `Category_name` y `category_number` 
  - no tienen el mismo numero de nulos (818, 284)
  - Se puede acceder a name a traves de number???
  - Finalmente dejamos los nulos como están

- `state_bottle_cost` , `state_bottle_retail` y `sale(dollars)` solo 10 nulos en cada columna, no se hace tratamiento de nulos, se dejan como tal

- `latitude` y `longitude`

##  Análisis

- Para analizar los datos lo mejor es generar visualizaciones.
  - Diferentes tipos para numéricas y categóricas.
- Creamos un df solo con las categóricas
```python
df_cat = df.select_dtypes(include='O)
```
- mejores visualizaciones para ver la distribucion de variables categóricas

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

- hacemos un subplot para ver todas las categóricas

````python
fig, axes = plt.subplots(5,2, figsize= (14,20))

for col in df_cat.columns:
     sns.countplot(data=df_cat, x=col, palette='mako', hue=col)
     ```

- coger una muestra mas pequeña para que no tarden tanto en ejecutarse 
```python
df = df.sample(2000) # tarda aprox 2 min
df = df.sample(1000) # tarda aprox 1 min
```

```python
fig, axes = plt.subplots(5,2, figsize= (14,20))

axes = axes.flatten()

for i,col in enumerate(df_cat.columns):
     sns.countplot(data=df_cat, x=col, palette='mako', hue=col, ax=axes[i])
     ```
- Como no se ve nada, vamos a rotar  los ejes
- Tampoco se ve, hacemos solo una columna con una visualizacion por fila
- Abortamos mision analisis de categoricas con graficas, hay tantas variables que es imposible ver nada