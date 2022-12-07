

class FSTreeNode:

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.size = 0
        self.children = []

    
    def __str__(self):
        return '({}, {}, {}, {})'.format(self.parent, self.name, self.size, len(self.children))


    def add_file(self, parent, name, size):
        # Add new file
        file = FSTreeNode(parent, name)
        file.size = int(size)
        self.children.append(file)
        
        # Update dir sizes
        while parent != None:
            parent.size += int(size)
            parent = parent.parent

    
    def add_dir(self, parent, name):
        # Add new dir
        self.children.append(FSTreeNode(parent, name))

def create_FSTreeNode(input_filename):
    # Return sum of the total sizes of directories which size <= 100,000    
    # Commands
    # cd /, cd x, cd ..
    # list -> (dir) dir x, (file) 123 abc

    sum_dir_lower_size = 0
    tree_top = FSTreeNode(None, '/')
    current_node = None    
    read_list = False

    with open(input_filename) as terminal:

        while True:
            line = terminal.readline().strip()
            if line == '': break
            
            if line[0] == '$':
                # Command
                command = line[2:]

                if command == 'ls':
                    continue
                elif command == 'cd /':
                    current_node = tree_top
                elif command == 'cd ..':
                    current_node = current_node.parent
                else:
                    # cd dir
                    node_name = command.split()[1]
                    for child in current_node.children:
                        if child.name == node_name:
                            current_node = child
                            #break
            else:
                # Listed element
                x, y = line.split()

                if x.isdigit():
                    # Add file
                    current_node.add_file(parent=current_node, name=y, size=x)
                else: 
                    # Add dir
                    current_node.add_dir(parent=current_node, name=y)

    return tree_top


def sum_total_size(current_node, max_size=100000):

    sum_total = 0

    # Reject files
    if len(current_node.children) == 0:
        return sum_total
    
    # If dir_size <= max_size
    if current_node.size <= max_size:
        sum_total += current_node.size

    # Add all children
    for child in current_node.children:
        sum_total += sum_total_size(child)

    return sum_total
    

def get_smallest_dir_to_delete(current_node, size_required=8381165):

    # Reject files
    # If dir_size < size_required not acceptable
    if len(current_node.children) == 0 or current_node.size < size_required:
        return None

    dir_deleted = current_node

    # Check all children
    for child in current_node.children:
        
        child_node = get_smallest_dir_to_delete(child)

        if child_node != None and child_node.size < dir_deleted.size:
            dir_deleted = child_node

    return dir_deleted


def main():
    tree_top = create_FSTreeNode('day_7_data.txt')
    # Exercise 1
    sum_size = sum_total_size(tree_top)
    print('Sum of dir\'s with size < 100e-3:', sum_size)
    # Exercise 2
    dir_deleted = get_smallest_dir_to_delete(tree_top)
    print('Delete dir {} occuping: {}'.format(dir_deleted.name, dir_deleted.size))


if __name__ == "__main__":
    main()