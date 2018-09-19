from pieces import *

"""
    This method returns list of piece (integer) with params file_name
    @params     file_name     (string)
    @returns    list of piece (list)
"""
def open_file(file_name):
    '''
        !!! Ganti jadi dictionary !!!
        Declare list of bidak
            list = [a,b,c,d]

            Value a untuk BISHOP
            Value b untuk KNIGHT
            Value c untuk QUEEN
            Value d untuk ROCK
    '''
    list = [0,0,0,0]

    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        # Input (asumsi input tanpa warna): KNIGHT 2 -> words = ["KNIGHT", 2]
        # Split it!
        words = line.split()

        if words[0].lower() == "bishop":
            list[0] += int(words[1])
        elif words[0].lower() == "knight":
            list[1] += int(words[1])
        elif words[0].lower() == "queen":
            list[2] += int(words[1])
        else:
            list[3] += int(words[1])

    return list

### Main
### Baca file dengan method raw_input
file_name = raw_input("Enter the file name: ");
print open_file(file_name)
