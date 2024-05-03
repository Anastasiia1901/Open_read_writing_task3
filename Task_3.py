import os

def add_combined_list(directory):
    file_list = os.listdir(directory)
    combined_list = []

    for file in file_list:
        with open(directory + "/" + file) as f:
            combined_list.append([file, 0, []])
            for line in f:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[2], reverse=True)


def create_general_file(directory, filename):
    with open(filename + '.txt', 'w+') as newfile:
        for file in add_combined_list(directory):
            newfile.write(f'File: {file[0]}\n')
            newfile.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('-------------------\n')


create_general_file('C:/Users/USER/Desktop/Open_read_file_3', 'general_file')


