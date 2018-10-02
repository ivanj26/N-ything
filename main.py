from Board import Board
from pieces import Bishop, Knight, Queen, Rook
from algorithm import HillClimbing, SimulatedAnnealing, GeneticAlgorithm
import os

def file_handler(file_name):
    """Create dictionary of chess pieces.

    Parameters
    ----------
    file_name : string
        Name of file.

    Returns
    -------
    dictionary
        Dictionary of chess pieces.
        Outputnya dictionary, contoh:
        {'WHITE KNIGHT': 2, 'WHITE ROOK': 2, 'WHITE QUEEN': 2, 'WHITE BISHOP': 2}
    """
    with open(file_name) as fin:
        file = []
        for line in fin.readlines():
            file.append(line.replace('\n', ''))

    file_encoded = [x.split() for x in file]

    result_dict = {}
    for line in file_encoded:
        result_dict[line[0] + ' ' + line[1]] = int(line[2])

    return result_dict

### MAIN ###
file_name = raw_input("Enter the file name: ")
request = file_handler(file_name)

print("Choose your desired algorithm..")
print("1. First Choice Hill Climbing")
print("2. Stochastic Hill Climbing")
print("3. Simulated Annealing")
print("4. Genetic Algorithm")
choice = int(raw_input("your choice :"))

if choice == 1:
    os.system("clear")
    max_attempt = int(raw_input("Insert max attempt :"))
    HillClimbing(request, 1, max_attempt)
elif choice == 2:
    os.system("clear")
    max_attempt = int(raw_input("Insert max attempt :"))
    HillClimbing(request, 2, max_attempt)
elif choice == 3:
    os.system("clear")
    max_attempt = int(raw_input("Insert max attempt :"))
    cooling_rate = float(raw_input("Insert cooling rate :"))
    temp = int(raw_input("Insert temperature :"))
    SimulatedAnnealing(request, max_attempt, cooling_rate, temp).start()
elif choice == 4:
    os.system("clear")
    max_attempt = int(raw_input("Insert max attempt :"))
    mutation_prob = float(raw_input("Insert mutation probability :"))
    max_generation = int(raw_input("Insert maximum number of generation :"))
    max_population = int(raw_input("Insert maximum number of population :"))
    GeneticAlgorithm(request, mutation_prob, 
        max_attempt, max_generation, max_population).start()


