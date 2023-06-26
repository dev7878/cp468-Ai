import random


def generate_chromosome(n):
    """Generate a random chromosome of length n."""
    return [random.randint(1, n) for _ in range(n)]


def fitness(chromosome):
    """Calculate the fitness of a chromosome, i.e. the number of non-attacking pairs of queens."""
    horizontal_collisions = sum(
        [chromosome.count(queen)-1 for queen in chromosome])/2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))


def probability(chromosome, fitness):
    """Calculate the probability of a chromosome being selected for crossover."""
    return fitness(chromosome) / maxFitness


def random_pick(population, probabilities):
    """Pick a random chromosome from the population for crossover."""
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w


def reproduce(x, y):
    """Perform crossover between two chromosomes."""
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


def mutate(x):
    """Randomly mutate a chromosome."""
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x


def genetic_queen(population, fitness):
    """Perform the genetic algorithm to find a solution to the n-queens problem."""
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities)
        child = reproduce(x, y)
        if random.random() < mutation_probability:
            child = mutate(child)
        new_population.append(child)
        if fitness(child) == maxFitness:
            break
    return new_population


def solve(nq):
    """Solve the n-queens problem."""
    global maxFitness
    maxFitness = nq*(nq-1)/2  # 8*7/2 = 28
    population = [generate_chromosome(nq) for _ in range(100)]

    while not maxFitness in [fitness(chrom) for chrom in population]:
        population = genetic_queen(population, fitness)
    chrom_out = []
    for chrom in population:
        if fitness(chrom) == maxFitness:
            chrom_out = chrom
            print_chromosome(chrom_out)
            break


def print_chromosome(chrom):
    """Print a chromosome."""
    print("Solution = {},  Fitness = {}"
          .format(str(chrom), fitness(chrom)))


# Run the solver.
solve(8)
