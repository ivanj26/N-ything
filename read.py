file_name = "input.txt"
def file_handler(file_name):
    with open(file_name) as fin:
        file = []
        for line in fin.readlines():
            file.append(line.replace('\n', ''))
    
    file_encoded = [x.split() for x in file]
    
    result_dict = {}
    for line in file_encoded:
        result_dict[line[0] + ' ' + line[1]] = int(line[2])
    
    return result_dict


file_handler(file_name)
