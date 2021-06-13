from GA.genetic import Genetic
from discretization.discretize import *
from Decision_Tree.create_tree import tree_score
from random import choices

class GeneticBinning(Genetic):
    def __init__(self):
        super().__init__()
        self.Genome = []                #list of bits
        
    def generate_genome(self):
        #Genome - representation of bins for all attributes
        #4 genes will represent a bin
        #first bit for each bin is type of binning
        #next three bits is the number of bins
        return choices([0,1], k= self.n_attr*4)   
    
    def fitness(self,genome):
        plist = [] 
        bin_optn = 0
        nbins = ''
        for i in range(len(genome)):
            if i%4==0:
                bin_optn = genome[i]  
            else:
                nbins += str(genome[i])
            if i%4==3:
                plist.append((bin_optn,nbins))
                nbins = ''
                
        df = discretize(plist)
        #print(df)
        fitness_score = tree_score(df)

        #store fitness scores in the dictionary
        self.fitness_dict[fitness_score] = genome
        print("".join(map(str,genome)), fitness_score)
        return fitness_score
                
    def genome_to_text(genome):
        pass


#gbin = GeneticBinning()
#gbin.run_evolution(20, .95, 20)
