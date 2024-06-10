import pandas as pd

# Criar um DataFrame de exemplo
data = {
    'feature1': [10, 20, 30],
    'feature2': [0.1, 0.2, 0.3],
    'tenho': [1, 0, 1],
    'feature3': ['A', 'B', 'C']
}

df = pd.DataFrame(data)
print("DataFrame Original:")
print(df)

# Nome da coluna alvo
target = 'tenho'

# Reordenar as colunas para colocar a coluna alvo na primeira posição
cols = [target] + [col for col in df.columns if col != target]
df = df[cols]

print("\nDataFrame com a Coluna Alvo na Primeira Posição:")
print(df)
