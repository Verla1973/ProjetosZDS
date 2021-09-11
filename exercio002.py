# O CEO da empresa House Rocket deseja saber o número de casas disponíveis para venda


import pandas as pd
data = pd.read_csv( 'datasets/kc_house_data.csv' )
print(f'{len(data)} casas estão disponíveis para venda...')

# Quantos atributos as casas possuem?

print(f'As casas possuem {data.shape[1]} atributos.')

# Quais são esses atributos?

print(f'Os atributos das casas são {data.columns}')

# Quantas casas possuem dois banheiros?

print(f'{len(data.query("bathrooms == 2"))} casas com dois banheiros.')

# Qual o preço médio de todas as casas?

print(f'O preço médio de todas as casas é de: {data["price"].mean():.2f}')

# Qual o preço médio das casas com dois banheiros?

print(f'Os preços médios das casas com dois banheiros é de: {data.query("bathrooms == 2")["price"].mean():.2f}')

# Qual o preço mínimo entre as casas com 3 quartos?

print(f'O preço mínimo das casas com 3 dormitórios é de: {data.query("bedrooms == 3")["price"].min()}...')

# Quantas casas possuem mais de 300mts2 na sala de estar?

print(f'{len(data.query("sqft_living > 3229"))} casas possuem mais de 300mts² de sala de estar...')

# Quantas casas possuem mais de dois andares?

print(f'{len(data.query("floors > 2"))} casas com mais de dois andares...')

# Quantas casas possuem frente para o mar?

print(f'{len(data.query("waterfront > 0"))} casas possuem frente para o mar...')

# Quantas casas possuem frente para o mar e possuem 3 quartos?


print(f'{len(data.query("waterfront > 0 and bedrooms == 3"))} casas possuem frente pro mar e '
      f'possuem três quartos...')

# Das casas com mais de 300mts² de sala de estar,quantas possuem mais de dois banheiros?

print(f'Das {len(data.query("sqft_living > 3229"))} casas com mais de 300mts² de sala de estar,'
      f'{len(data.query("sqft_living > 3229 and bathrooms > 2"))} '
      f'possuem mais de dois banheiros...')
