from FIS.fis_prediction import FISPREDICT
import pandas as pd

def fis_score():
    fobj = FISPREDICT()
    total_error = 0
    df = pd.read_csv('Testing/transformed_dataset.csv')
    target = df['BTC_PRICE']
    
    for i in range(1, len(df)):
        mean = df['MEAN'][i]
        median = df['MEDIAN'][i]
        trend = df['TREND'][i]
        pbtc = df['PBTC'][i]
        
        try:
            p_value = fobj.predict(mean, median, trend, pbtc)
        except ValueError:
            p_value = pbtc
        total_error += abs(p_value - float(target[i]))/float(target[i])
    
    mean_error = total_error/len(df)
    return mean_error

#fis_score()
    
