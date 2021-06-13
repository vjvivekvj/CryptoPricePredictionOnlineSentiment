from discretization.discretization import Discretize
import pandas as pd

fname = Discretize.csv_input
input_df = pd.read_csv(fname)
input_df = input_df.drop('BTC_PRICE', axis = 'columns')
output_df =  pd.DataFrame(columns = input_df.columns)
col_list = output_df.columns.tolist()

def discretize(plist):              #plist is the list of tuples
    global output_df
    attr = 0
    for tup in plist:
        input_attr = input_df[col_list[attr]]
        input_attr = input_attr.to_frame()
        dobj = Discretize(input_attr)
        nbins = int(tup[1], 2)
        if nbins < 2:
            nbins = 2
       # print(nbins)
        bin_opt = tup[0]
        if bin_opt == 0:
            temp_df = Discretize.equiwidth_binning(dobj,nbins) 
        else:
            temp_df = Discretize.equifrequency_binning(dobj,nbins)
        output_df[col_list[attr]] = temp_df[col_list[attr]]
        attr += 1
    return output_df        

#obj = Discretize()
#obj.df