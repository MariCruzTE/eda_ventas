# Preanalisis de los datos

- `date`, cambiar a formato fecha
- `store_location` necesita descomposicion en nuevas columnas, esta en mayusculas
- `county_number` , pasar de float a int, hay valores Nan y no se puede cambiar el tipo de datos antes del tratamiento de nulos
- `category`, deberia ser category_number y pasar de float a int , hay valores Nan y no se puede cambiar el tipo de datos antes del tratamiento de nulos
- `vendor_number`, pasar de float a int
- `state_bottle_cost`, de object a float, eliminar $
- `state_bottle_retail`,de object a float, eliminar $
- `sale(dollars)`,de object a float, eliminar $

## Normalizacion de datos
- tenemos dos columnas que miden el volumen en distintas unidades,('`bottle_volume(ml)` y `volume_sold(gallons)` ') hay que unificar a una misma unidad
