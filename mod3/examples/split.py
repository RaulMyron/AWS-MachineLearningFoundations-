import pandas as pd
from sklearn.model_selection import train_test_split

# Create some sample data
data = {'Idade': [30, 25, 40, 32, 28], 'Sexo': ['M', 'F', 'M', 'F', 'M'], 'Dindin': [50000, 42000, 78000, 61000, 53000]}
df = pd.DataFrame(data)

# Print the original data
print("Original Data:")
print(df)

# Split the data into training and testing sets
train, test = train_test_split(df, test_size=.3, random_state=42, stratify=df['Sexo'])

# Print the training data 70%
print("\nTraining Data:")
print(train)

# Print the testing data 30%
print("\nTesting Data:")
print(test)
