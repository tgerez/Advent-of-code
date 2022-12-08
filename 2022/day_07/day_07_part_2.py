"""

--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

    Delete directory e, which would increase unused space by 584.
    Delete directory a, which would increase unused space by 94853.
    Delete directory d, which would increase unused space by 24933642.
    Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?


"""

# Création de classes simples
class Directory:
    """ Directories have a name and a path
    They have also a size
    """
    pass

class File:
    """ Files have a name, a size and a path
    """
    pass


def size_folder_calculation(folder, files):
    """ Take in argument a folder object and the files list
    It modifies the folder
    """
    for f in files:
        if folder.path + folder.name == f.path[:len(folder.path + folder.name)]:
            folder.size += f.size

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    
    #############
    #
    # Construction of file system Tree
    #
    #############
    
    # Adding a stop caracter at the end of the file
    data_list.append('$')
    
    current_path = ''
    
    directories = []
    files = []
    
    for i, line in enumerate(data_list):
        
        # Checking command
        if line[0] == '$':
            
            # List content
            if line[2:4] == 'ls':
                """ We will scan all lines after the ls command
                until we see a new command line 
                """
                j = 1
                while data_list[i+j][0] != '$': # will compulsory stop at the end of file thanks to adding a a stop caracter
                    # finding directory
                    if data_list[i+j][0:3] == 'dir':
                        directories.append(Directory())
                        directories[-1].name = data_list[i+j][4:]
                        directories[-1].path = current_path
                        directories[-1].size = 0
                        
                    # finding a file
                    else:
                        # collect file infos
                        f = data_list[i+j].split()
                        size = int(f[0])
                        name = f[1]
                        # creating file
                        files.append(File())
                        files[-1].size = size
                        files[-1].name = name
                        files[-1].path = current_path
                    
                    # go to next line
                    j += 1
                
            
            # Change directory
            elif line[2:4] == 'cd':
                
                # Go to root
                if line[5:] == '/':
                    current_path = '/'
                
                # Entering subfolder
                elif line[5:] != '..':
                    current_path += line[5:] + '/'
                
                # go up to parent folder
                else:
                    current_path = current_path.split('/')
                    current_path.pop(-2) # 0 and -1 positions are occupied by empty strings
                    current_path = '/'.join(current_path) # new path starts and ends with / thanks to presence of empty strings in the list above
                
    
    #############
    #
    # Calculating folders size
    #
    #############
    
    for folder in directories:
        size_folder_calculation(folder, files)
    
    
    #############
    #
    # Saving space
    #
    #############
    
    root_size = 0
    
    for f in files:
        root_size += f.size
    
    empty_space = 70000000 - root_size
    min_size_of_folder_to_be_deleted = 30000000 - empty_space
    
    directories_sizes = []
    
    for d in directories:
        directories_sizes.append(d.size)
    
    for s in sorted(directories_sizes):
        if s >= min_size_of_folder_to_be_deleted:
            return s
    


print(resolve_problem('day_07_test_input'))
print(resolve_problem('day_07_my_input'))



