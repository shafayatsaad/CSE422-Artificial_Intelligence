import numpy as np

class GeneticAlgorithm:
    def __init__(self, target, population_size, mutation_rate, num_generations, players):
        self.target = target
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.players = players

    def fitness(self, individual):
        return abs(self.target - np.sum(individual * self.players))

    def mutate(self, individual):
        index = np.random.randint(len(individual))
        individual[index] = 1 - individual[index]
        return individual

    def crossover(self, parent1, parent2):
        child = np.concatenate((parent1[:len(parent1)//2], parent2[len(parent1)//2:]))
        return child

    def run(self):
        population = np.random.randint(2, size=(self.population_size, len(self.players)))

        for generation in range(self.num_generations):
            population = sorted(population, key=self.fitness)

            if self.fitness(population[0]) == 0:
                return population[0]

            next_generation = population[:2]

            for i in range(len(population) // 2 - 1):
                parent1 = population[np.random.choice(len(population))]
                parent2 = population[np.random.choice(len(population))]
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)

                next_generation += [self.mutate(child1), self.mutate(child2)]

            population = next_generation

    
        return population[0]

N, T = map(int, input().split())
players_data = []
for i in range(N):
    name, avg_run = input().split()
    players_data.append((name, int(avg_run)))

player_names, avg_runs = zip(*players_data)
avg_runs = np.array(avg_runs)

population_size = 100
mutation_rate = 0.01
num_generations = 1000

ga = GeneticAlgorithm(T, population_size, mutation_rate, num_generations, avg_runs)
result = ga.run()

print(list(player_names))
if ga.fitness(result) != 0:
    print(-1)
else:
    print(''.join(map(str,result)))
