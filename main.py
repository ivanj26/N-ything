from pieces import *
from Board import Board

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


### Main
### Baca file dengan method raw_input
# file_name = raw_input("Enter the file name: ")
file_name = 'input.txt'
print file_handler(file_name)

### Board test cases
request = file_handler(file_name)
board = Board(request)
print 'Heuristic: ', board.calculate_heuristic()
print board.draw()
print board.print_all_pieces()