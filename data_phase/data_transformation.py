import pandas as pd
csv_input = pd.read_csv('results/cleaned_dataset.csv')

price = 'BTC_PRICE'
changes = [0]
pchange = [0]
trend = [0]
for i in range(1,len(csv_input)):
    if csv_input[price][i] - csv_input[price][i-1] > 0:
        changes.append(1)
        trend.append(trend[-1]+1)
        
    elif csv_input[price][i] - csv_input[price][i-1] < 0:
        changes.append(-1)
        trend.append(trend[-1]-1)
    else:
        changes.append(0)
        trend.append(trend[-1])
    
    _pchange = ((csv_input[price][i] - csv_input[price][i-1])/csv_input[price][i-1]) * 100
    pchange.append("{:.2f}".format(_pchange))
    
    
csv_input['CHANGE'] = changes
csv_input['PCHANGE'] = pchange
csv_input['TREND'] = trend
    
csv_input.to_csv('results/transformed_dataset.csv', index=False)
