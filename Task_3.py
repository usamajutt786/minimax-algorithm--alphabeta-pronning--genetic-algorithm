import random

def target_function(x):
    if x is None:
        return float('-inf')
    return x**2+8.8

POPULATION_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.1

def initialize_individual():
    return random.uniform(-5, 5)

def evaluate_fitness(individual):
    return target_function(individual)

def roulette_wheel_selection(population,fitness_value):
    total_fitness=sum(fitness_value)
    selected_value=random.uniform(0,total_fitness)
    cumulative_fitness=0
    for i in range(len(population)):
        cumulative_fitness+=fitness_value[i]
        if cumulative_fitness>selected_value:
            return population[i]

def crossover(parent1,parent2):
    if parent1 is None or parent2 is None:
        return initialize_individual()
    crossover_point=random.uniform(-5,5)
    child =(parent1 + parent2)
    return child

def mutate(individual):
    mutation_value=random.uniform(-0.5,0.5)
    return individual+mutation_value

def genetic_algorithm(population_size,num_generation,mutation_rate):
    population=[initialize_individual() for _ in range(population_size)]
    best_individual=None
    best_fitness=float('-inf')
    all_best_fitness=[]
    for generation in range(num_generation):
        fitness_values=[evaluate_fitness(individual) for individual in population]
        parents=[roulette_wheel_selection(population,fitness_values) for _ in range(population_size)]
        offspring=[crossover(parents[i% population_size],parents[(i+1)% population_size]) for i in range(population_size)]
        offspring=[mutate(individual) if random.random() < mutation_rate else individual for individual in offspring]
        population=parents+offspring
        current_best_index=fitness_values.index(max(fitness_values))
        current_best_fitness=fitness_values[current_best_index]

        if current_best_fitness > best_fitness:
            best_individual=population[current_best_index]
            best_fitness=current_best_fitness

        all_best_fitness.append(best_fitness)

        print(f'Generation {generation}: Best Fitness = {best_fitness:.4f}')
    return best_individual

result=genetic_algorithm(POPULATION_SIZE,GENERATIONS,MUTATION_RATE)
print(f'\nOptimal Solution: {result}')
print(f'\nOptimal Fitness :{evaluate_fitness(result):.4f}')