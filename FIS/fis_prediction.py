from FIS.fis_r import FIS

import skfuzzy as fuzzy
from skfuzzy import control as ctrl

class FISPREDICT(FIS):
    
    def __init__(self):
        super().__init__()
        self.initialize_fis()
        
    def predict(self, MEAN, MEDIAN, TREND, PBTC):

        self.price.input[self.col_input[0]] = MEAN
        self.price.input[self.col_input[1]] = MEDIAN
        self.price.input[self.col_input[2]] = TREND
        self.price.input[self.col_input[3]] = PBTC
        
        self.price.compute()
        return self.price.output['BTC_PRICE']
                        

        
#fpredict = FISPREDICT()
        #### GRAPH ####
#    fpredict.draw_graph(fpredict.antecedent_dict[i])
        ### PREDICTION ###
#fpredict.predict(0.26,0.25,0,9988.07) 
