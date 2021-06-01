import pandas as pd
csv_input = pd.read_csv('cleaned_dataset.csv')

price = 'BTC_PRICE'
changes = [0]
for i in range(1,len(csv_input)):
    if csv_input[price][i] - csv_input[price][i-1] > 0:
        changes.append(1)
    elif csv_input[price][i] - csv_input[price][i-1] < 0:
        changes.append(-1)
    else:
        changes.append(0)
    
csv_input['CHANGE'] = changes
    
csv_input.to_csv('transformed.csv', index=False)
