import random
import numpy as np


def make_population(size):
    pop = []
    for _ in range(size):
        pop.append(random.sample(range(-50, 50), 3))

    return pop


def read_data():
    x = np.genfromtxt('x_train.csv', delimiter=',')
    y = np.genfromtxt('y_train.csv', delimiter=',')
    return x, y


def cal_fitness(chromosome):
    a, b, c = chromosome[0], chromosome[1], chromosome[2]
    y_train = []
    for x in x_train:
        y_train.append(a * (x ** 2) + b * x + c)

    offset = np.subtract(y_train, y_test)
    offset = abs(offset)
    total_offset = np.sum(offset)

    return total_offset / len(x_train)


def crossover(chromosome_1, chromosome_2):
    first_child = chromosome_1
    first_child[0] = chromosome_2[0]
    second_child = chromosome_2
    second_child[0] = chromosome_1[0]
    return first_child, second_child


def mutation(chromosome):
    chromosome[0] = random.uniform(-50, 50)
    return chromosome


def run_genetic():
    for _ in range(100):
        fitness_values = []
        sample1 = random.randint(0, 499)
        sample2 = random.randint(0, 499)
        firstchild, secondchild = crossover(population[sample1], population[sample2])
        secondchild = mutation(secondchild)
        # Choose 2 random parents
        # Crossover two parents
        # Mutate one of the parents
        # Swap two children with two worst chromosome in population
        for p in population:
            fitness_values.append((cal_fitness(p)))
        fitness_values = np.argsort(fitness_values)
        population[fitness_values[499]] = firstchild
        population[fitness_values[498]] = secondchild
        # For this, calculate all chromosomes in population, then sort them based on their fitness
        # Repeat
    fitness_values = []
    for p in population:
        fitness_values.append((cal_fitness(p)))
    temp = fitness_values
    temp = np.sort(temp)
    fitness_values = np.argsort(fitness_values)
    print(temp[0])
    print(temp[499])
    print(population[fitness_values[0]])

    return


if __name__ == '__main__':
    population = make_population(500)
    x_train, y_test = read_data()
    run_genetic()
