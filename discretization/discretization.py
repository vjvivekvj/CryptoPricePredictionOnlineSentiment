import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer


class Discretize:
    csv_input = "data_phase/results/transformed_dataset.csv"
    df = pd.read_csv(csv_input) 
    
    def __init__(self):
        self.input = Discretize.df.drop('CHANGE',axis='columns')    
        
    def df_to_csv(self, dataframe):
        dataframe.to_csv (r'discretized_dataframe.csv', index = False, header=True)
        
    def pandas_dframe(self, np_discretized):
        discretized_dataframe = pd.DataFrame.from_records(np_discretized)
        discretized_dataframe.columns = self.input.columns
        self.df_to_csv(discretized_dataframe)
        return discretized_dataframe

        
    def equiwidth_binning(self, bins, pandas_df=True, df_to_csv=False):
        discretizer = KBinsDiscretizer(n_bins=bins, encode = 'ordinal', strategy='uniform')
        discretized_data = discretizer.fit_transform(self.input)
        if pandas_df:
            return self.pandas_dframe(discretized_data)
        else:
            return discretized_data
        
    def equifrequency_bining(self, bins, input_df=input, pandas_df=True,df_to_csv=False):
        discretizer = KBinsDiscretizer(n_bins=bins , encode = 'ordinal', strategy='quantile')
        discretized_data = discretizer.fit_transform(input_df)
        if pandas_df:
            return self.pandas_dframe(discretized_data)
        else:
            return discretized_data

#dobj = Discretize()
#dobj.input
#dobj.equiwidth_binning(5)
