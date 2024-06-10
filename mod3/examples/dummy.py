import pandas as pd

# Criando um DataFrame com uma coluna categórica
df = pd.DataFrame({'categoria': ['A', 'B', 'A', 'C', 'B']})

# Convertendo a coluna 'categoria' em variáveis dummy
df_dummy = pd.get_dummies(df['categoria'],dtype=int)

# Exibindo o DataFrame com variáveis dummy
print(df_dummy)
