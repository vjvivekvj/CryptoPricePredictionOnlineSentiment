import pandas as pd
from sklearn import tree
from sklearn.tree import _tree

default_df = pd.read_csv("discretization/results/discretized_dataframe.csv")
input_df = default_df.drop('BTC_PRICE', axis='columns')
target_df= default_df['BTC_PRICE']


class DTree:
        
    def __init__(self):
        self.model = tree.DecisionTreeClassifier()
        self.isFit = False
        self.rule_list = []
        self.ante_list = []
        self.conse_list = []
        
    def generate_model(self, inputs=input_df, target=target_df):
        self.model.fit(inputs, target)
        self.isFit = True
    
    def model_score(self,inputs=input_df,target=target_df):
        if self.isFit:
            return self.model.score(inputs,target)
        else:
            print("Fit the model first")
    
    def tree_to_code(self,tree, feature_names):
        tree_ = tree.tree_
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]
        def recurse(node, depth):
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                self.ante_list.append((name, threshold))
                recurse(tree_.children_left[node], depth + 1)
                self.ante_list.append((name,threshold))
               # print(self.ante_list)
                recurse(tree_.children_right[node], depth + 1)
            else:
                self.rule_list.append(self.ante_list)
                #print(self.rule_list)
                #print('/n')
                self.ante_list = []
                self.conse_list.append(tree_.value[node])
        recurse(0, 1)
        return self.rule_list, self.conse_list
    
    def create_rules(self):
        rules_df = input_df.drop('SUM', axis='columns')
        rules_df = rules_df.drop('COUNT', axis='columns')
        rules_df = rules_df.drop('CHANGE', axis='columns')
        rules_df = rules_df.drop('PCHANGE', axis='columns')
      
        if not self.isFit:
            self.generate_model(inputs = rules_df, target = target_df)
    
        return self.tree_to_code(self.model, rules_df.columns.tolist())
    
#dobj = DTree()
#dobj.create_rules()
