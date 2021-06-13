from random import choices
from random import randint
from random import sample
from random import random



class Genetic:
    
    def __init__(self):
        self.population = []            #list of genomes
        self.mutation_rate = 0.2
        self.fitness_dict = {}
        self.n_attr = 8

        
    def create_population(self, size):
        #call generate genome
        #append genome to the population
        self.size = size
        for _ in range(size):
            self.population.append(self.generate_genome())
    
    def selection(self):
        sorted_fit = sorted(self.fitness_dict.keys())
        i = 0
        self.population = []
        #add 25% fittest 
        for g in sorted_fit:
            self.population.append(self.fitness_dict[g]) 
            i += 1
            if(i >= len(sorted_fit)/4):
                break
        #add 25% random (remaining 50% child by doing crossover())
        self.create_population(int(len(sorted_fit)/2) - i)
        
    
    def crossover(self):
        for i in range((self.size - len(self.population))//2):
            #select two parents randomly
            parent = sample(self.population,2)
            a = parent[0] ; b = parent[1]
            #select a random crossover point
            p = randint(1, len(self.population)-1)
            #add children to the population
            self.population.append(a[:p]+ b[p:])
            self.population.append(b[:p] + a[p:])
            
            
    def mutation(self):
        #pick a random genome 
        genome = sample(self.population,1)
        #pick a random index and change its bit
        #index = randint(1, len(genome)-1)
        index = 0
        if random() < self.mutation_rate:
            genome[index] = abs(genome[index]-1)
        
    
    def run_evolution(self, p_size, f_min, g_max):
        generation = 0
        for i in range(g_max):
            generation+= 1 
            
            self.create_population(p_size)
            for genome in self.population:
              #  print('checking ', genome)
                if self.fitness(genome) >= f_min:
                    print('genome with given fmin found ', "".join(map(str,genome)), ' in ', generation, ' generation')
                    return ("".join(map(str,genome)),self.fitness(genome),generation)
            # create new population         - selection selects the genomes for new population
            self.selection()
            # add more children             - crossover adds new genomes in the new population
            self.crossover()
            # mutate                        - mutation flips genes of a random genome
            #self.mutation()                - theres some error , will be fixed 
            
            if generation >= g_max:
                print('no genome with given fitness value found')
                print('Increase no. of generations or dec fmin')
                return (0,0,0)
            
            self.fitness_dict = {} 
        return
            
            
            
            
