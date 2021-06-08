import pandas as pd
from Decision_Tree.decision_tree import DTree


def tree_score(df):

    target_f = pd.read_csv("data_phase/results/transformed_dataset.csv")
    target = target_f['CHANGE']

    
    tobj = DTree()
    
    tobj.generate_model(df,target)
    return tobj.model_score(df, target)