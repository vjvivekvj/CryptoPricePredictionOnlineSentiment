from GA.genetic import Genetic
from random import choices
import pandas as pd
from discretization.discretization import Discretize
from Decision_Tree.create_tree import tree_score

class GeneticFeatures(Genetic):
    csv_input = "data_phase/results/transformed_dataset.csv"
    temp_df = pd.read_csv(csv_input)
    temp_df = temp_df.drop('BTC_PRICE', axis = 'columns')
    features = temp_df.columns.tolist()
    
    def __init__(self):
        super().__init__()
        self.Genome = []                #list of bits
        
    def generate_genome(self):
        return choices([0,1], k= self.n_attr)
    
    def fitness(self, genome):
        input_df = pd.DataFrame()
        for i in range(len(genome)):
            if genome[i]:
                input_df[GeneticFeatures.features[i]]= GeneticFeatures.temp_df[GeneticFeatures.features[i]]
        if len(input_df.columns.tolist()) > 0:
            dobj = Discretize(input_df)
            discretized_df = dobj.equifrequency_binning(5)
            fitness_score = tree_score(discretized_df)
            print("".join(map(str,genome)), fitness_score)
            self.fitness_dict[fitness_score] = genome
            return fitness_score
        
        else:
            return 0
        
    
        

#gobj = GeneticFeatures()
#print(gobj.generate_genome())
#gobj.fitness([1,0,1,0,1,0,1])

#gobj.run_evolution(50, .97, 20)
