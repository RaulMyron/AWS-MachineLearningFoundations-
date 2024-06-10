import pandas as pd

# Exemplo de DataFrame (assumindo que 'InvoiceDate' é uma coluna de string)
retail = pd.DataFrame({'InvoiceDate': ['01/01/2023', '02/02/2023', '03/03/2023', '03/03/2023']})

# Converter 'InvoiceDate' para formato de data (assumindo formato DD/MM/AAAA)
retail['InvoiceDate'] = pd.to_datetime(retail['InvoiceDate'], format='%d/%m/%Y')

print("-"*15)
print(retail)
# Assumindo que o DataFrame 'retail' tenha formato de data para 'InvoiceDate'
# Definir 'InvoiceDate' como índice
retail = retail.set_index('InvoiceDate')
print("-"*15)
print(retail)
