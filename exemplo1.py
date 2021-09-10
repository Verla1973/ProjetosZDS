# Carregue o conjunto de dados contido no arquivo kc_house_data.csv
# Função = read_csv
# Biblioteca = pandas


import pandas as pd
data = pd.read_csv( 'datasets/kc_house_data.csv' )
#print(data)

# Mostre na tela o conjunto de dados ordenados pela coluna 'price',só mostrar id e price

print( data[['id', 'price']].sort_values('price') )

# Mostre na tela o conjunto de dados ordenados pela coluna 'price',do maior para o menor.

print( data[['id', 'price']].sort_values('price', ascending=False))
