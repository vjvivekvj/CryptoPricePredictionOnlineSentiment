import pandas as pd
from sklearn import tree

class DTree:
        
    def __init__(self):
        self.model = tree.DecisionTreeClassifier()
        self.isFit = False
    def generate_model(self, input, target):
        self.model.fit(input, target)
        self.isFit = True
    
    def model_score(self,inputs,target):
        if self.isFit:
            return self.model.score(inputs,target)
        else:
            print("Fit the model first")
    
    def create_ruleset(self):
        pass
    
    
