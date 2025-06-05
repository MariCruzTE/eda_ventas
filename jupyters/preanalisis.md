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

- `state_bottle_cost` , `state_bottle_retail` y `sale(dollars)` solo 10 nulos en cada columna, no se hace tratamiento de nulos, se dejan como tal

- `latitude` y `longitude`
  - 