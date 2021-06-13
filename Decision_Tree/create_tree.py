import pandas as pd
from Decision_Tree.decision_tree import DTree

default_df = pd.read_csv("discretization/results/discretized_dataframe.csv")
default_df = default_df.drop('BTC_PRICE', axis = 'columns')

def tree_score(df = default_df):

    target_f = pd.read_csv("discretization/results/discretized_dataframe.csv")
    target = target_f['BTC_PRICE']

    #print(df.head())
    tobj = DTree()
    #print(df)
    tobj.generate_model(df,target)
    return tobj.model_score(df, target)

#tree_score()