import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer


class Discretize:
    csv_input = "data_phase/results/transformed_dataset.csv"
    df = pd.read_csv(csv_input) 
    
    def __init__(self,input=df):
        self.input = input
        #self.input = Discretize.df.drop('CHANGE',axis='columns')    
        
    def df_to_csv(self, dataframe):
        dataframe.to_csv (r'discretization/results/discretized_dataframe.csv', index = False, header=True)
        
    def pandas_dframe(self, np_discretized, df_to_csv):
        discretized_dataframe = pd.DataFrame.from_records(np_discretized)
        discretized_dataframe.columns = self.input.columns
        if df_to_csv:
            self.df_to_csv(discretized_dataframe)
        return discretized_dataframe

        
    def equiwidth_binning(self, bins, df_to_csv=False, pandas_df=True):
        discretizer = KBinsDiscretizer(n_bins=bins, encode = 'ordinal', strategy='uniform')
        discretized_data = discretizer.fit_transform(self.input)
        to_csv = df_to_csv
        if pandas_df:
            return self.pandas_dframe(discretized_data, to_csv)
        else:
            return discretized_data
        
    def equifrequency_binning(self, bins, df_to_csv=False, pandas_df=True):
        discretizer = KBinsDiscretizer(n_bins=bins , encode = 'ordinal', strategy='quantile')
        discretized_data = discretizer.fit_transform(self.input)
        to_csv = df_to_csv
        if pandas_df:
            return self.pandas_dframe(discretized_data, to_csv)
        else:
            return discretized_data

#dobj = Discretize()
#dobj.input
#dobj.equiwidth_binning(3,True)
