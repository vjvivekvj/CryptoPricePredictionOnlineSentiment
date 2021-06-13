import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import pandas as pd

class FIS:
    csv_input = "data_phase/results/transformed_dataset.csv"
    default_df = pd.read_csv(csv_input)
    default_df = default_df.drop('SUM', axis='columns')
    default_df = default_df.drop('COUNT', axis='columns')
    #conse_df = default_df['BTC_PRICE']
    default_df = default_df.drop('PCHANGE', axis='columns')
    default_df = default_df.drop('CHANGE', axis='columns')
    def __init__(self, df = default_df):
        self.df = df
        self.col_input = df.drop('BTC_PRICE', axis='columns').columns.tolist() 
        self.antecedent_dict = {}
        self.CryptoPredictor = ctrl.ControlSystem()        
        self.itr = 0
        
    def add_antecedent(self, antecedent, n_sets = 5):
        #if antecedent == 'BTC_PRICE':
         #   return
        print('adding antecedent ', antecedent)
        maxval = self.df[antecedent].max()
        minval = self.df[antecedent].min()
        #print(minval, maxval)
        universe = np.arange(minval, maxval, 0.2)
        self.antecedent_dict[antecedent] = ctrl.Antecedent(universe, self.col_input[self.itr])
        self.antecedent_dict[antecedent].automf(n_sets)
        self.itr += 1
        #self.draw_graph(self.antecedent_dict[antecedent])
    
    def create_antecedents(self):
        for antecedent in self.col_input:
            self.add_antecedent(antecedent)
        return 
    
    def create_consequent(self):
        print('adding consequent')
        maxval = self.df['BTC_PRICE'].max()
        minval = self.df['BTC_PRICE'].min()
        universe = np.arange(minval, maxval, 1)
        self.conse = ctrl.Consequent(universe, 'BTC_PRICE')
        self.conse.automf(5)
        #self.draw_graph(self.conse)

    def add_rule(self):

        rule = []
        rule.append(ctrl.Rule(self.antecedent_dict['PBTC']['poor'] & self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] , self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] , self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['poor'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['average'], self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] & self.antecedent_dict['MEDIAN']['decent'], self.conse['poor']))
         
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] & self.antecedent_dict['MEDIAN']['decent'], self.conse['poor'])) 
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] & self.antecedent_dict['MEDIAN']['decent'], self.conse['poor']))
         
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['poor']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['PBTC']['poor'] & self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['poor'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['poor'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['mediocre'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['poor'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['mediocre'] & self.antecedent_dict['MEDIAN']['average'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] & self.antecedent_dict['MEDIAN']['average'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] & self.antecedent_dict['MEDIAN']['decent'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['mediocre'] & self.antecedent_dict['MEAN']['average'] & self.antecedent_dict['MEDIAN']['decent'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] & self.antecedent_dict['MEDIAN']['average'], self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['poor'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['decent'] , self.conse['mediocre']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] & self.antecedent_dict['MEDIAN']['average'], self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['average'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] & self.antecedent_dict['MEDIAN']['mediocre'], self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent']  & self.antecedent_dict['MEDIAN']['average'], self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent']  & self.antecedent_dict['MEDIAN']['decent'], self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] , self.conse['average']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['mediocre'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['decent'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['decent'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['average'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['poor'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] & self.antecedent_dict['MEDIAN']['average'], self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] & self.antecedent_dict['MEDIAN']['average'], self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] & self.antecedent_dict['MEDIAN']['average'], self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['decent'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['decent'] , self.conse['decent']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['PBTC']['decent'] & self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['poor'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['mediocre'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['mediocre'] & self.antecedent_dict['MEAN']['mediocre'] & self.antecedent_dict['MEDIAN']['average'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['average'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['decent'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['average'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] & self.antecedent_dict['MEAN']['mediocre'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['mediocre'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] & self.antecedent_dict['MEDIAN']['mediocre'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['mediocre'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEAN']['mediocre'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] & self.antecedent_dict['MEDIAN']['average'], self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['TREND']['decent'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['average'] , self.conse['good']))
        
        rule.append(ctrl.Rule(self.antecedent_dict['MEDIAN']['decent'] , self.conse['good']))
        #rule1 = ctrl.Rule(self.antecedent_dict['PBTC']['poor'] & self.antecedent_dict['TREND']['poor'] & self.antecedent_dict['MEAN']['poor'] & self.antecedent_dict['MEDIAN']['poor'], self.conse['poor'])
        #self.CryptoPredictor.addrule(rule1)
        for i in range(len(rule)):
            self.CryptoPredictor.addrule(rule[i])
        
    def draw_graph(self, x):
        x.view()
        
    def initialize_fis(self):
        self.create_consequent()
        self.create_antecedents()
        self.add_rule()
        self.price = ctrl.ControlSystemSimulation(self.CryptoPredictor)
    
#fuzobj = FIS()
##fuzobj.create_antecedents()
#fuzobj.create_consequent()
#fuzobj.add_rule()