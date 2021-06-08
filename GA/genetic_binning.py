from GA.genetic import *
from discretization.discretize import *
from Decision_Tree.create_tree import tree_score

class GeneticBinning(Genetic):
    def __init__(self):
        super().__init__()
        
    def fitness(self,genome):
        plist = [] 
        bin_optn = 0
        nbins = ''
        for i in range(len(genome)):
            nbins += str(genome[i])
            if i%4==0:
                bin_optn = genome[i]  
            if i%4==3:
                plist.append((bin_optn,nbins))
                nbins = ''
                
        df = discretize(plist)
        fitness_score = tree_score(df)

        #store fitness scores in the dictionary
        self.fitness_dict[fitness_score] = genome
        print("".join(map(str,genome)), fitness_score)
        return fitness_score
                
    def genome_to_text(genome):
        pass


gbin = GeneticBinning()
gbin.run_evolution(20, .90, 20)
