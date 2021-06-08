from GA.genetic import *
from discretization.discretize import *
from Decision_Tree.create_tree import tree_score

class GeneticBinning(Genetic):
    def __init__(self):
        super().__init__()
        
    def fitness(self):
        for genome in self.population:
            plist = [] 
            bin_opt = 0
            nbins = ''
            for i in range(len(genome)):
                nbins += str(genome[i])
                if i%4==0:
                    bin_opt = genome[i]  
                if i%4==3:
                    plist.append((bin_opt,nbins))
                    nbins = ''
            df = discretize(plist)
            fitness_score = tree_score(df)
            print("".join(map(str,genome)), fitness_score)
        return
                

gbin = GeneticBinning()
gbin.create_population(2) #user input
gbin.fitness()