from random import choices

n_attr = 8 

class Genetic:
    
    def __init__(self):
        self.Genome = []                #list of bits
        self.population = []            #list of genomes
        self.mutation_rate = 0.1
        
    def generate_genome(self):
        #Genome - representation of bins for all attributes
        #4 genes will represent a bin
        #first bit for each bin is type of binning
        #next three bits is the number of bins
        return choices([0,1], k= n_attr*4)
        
    def create_population(self, size):
        #call generate genome
        #append genome to the population
        for _ in range(size):
            self.population.append(self.generate_genome())
    
    def selection():
        pass
    
    def crossover():
        pass
    
    def mutation():
        pass
    
