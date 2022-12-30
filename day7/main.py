# For this implemenation I wanted to practice using inheritance, type hinting and some recursive 
# tree navigation. I also explored PEP naming conventions and woreked on a better understanding of Python

# Parent super class for shared attributes of file system elements
class FileSystem:
    def __init__(self, name) -> None:
        self.name = name
        self.parent = self
           
    def getParent(self) :
        return self.parent
    
    def setParent(self, parent: "Directory"):
        self.parent = parent
        
    def getName(self) -> str:
        return self.name
  
# Directory is an element of the filesystem that contains other elements.        
class Directory(FileSystem):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.contents = []
    
    def addItem(self, item: "FileSystem") -> int:
        item.setParent(self)
        self.contents.append(item)
        return len(self.contents)
    
    def getSize(self) -> int:
        size = 0
        for item in self.contents:
            size += item.getSize()
        return size
    
    # generates a list of directories with a size under a certain value
    def get_dirs_under(self, max_size, result):
        #result = list()
        if self.getSize() <= max_size:
            result.append(self)
        for item in self.contents:
            if type(item) == Directory:
                item.get_dirs_under(max_size, result)
                
    def get_dirs_over(self, min_size, result):
        if self.getSize() >= min_size:
            result.append(self)
        for item in self.contents:
            if type(item) == Directory:
                item.get_dirs_over(min_size, result)
    
    # creates a string representation of the tree with a csv friendly format for troublshooting
    def format_tree(self, level = 0):
        out = ""
        if level == 0:
            out += str("d,%d,%sName %s\n" %(self.getSize(),","*level,  self.getName()))
        # Group folders and directories
        for item in self.contents:
            if type(item) == File:
                out += str("f,%d,%sName %s\n" %(item.getSize(), ","*(level+1), item.getName()))
        for item in self.contents:
            if type(item) == Directory:
                out += str("d,%d,%sName %s\n" %(item.getSize(), ","*(level+1), item.getName()))
                out += item.format_tree(level+ 1)
        return out
    
    # Maybe not the best place for this, used to return a related directory
    def change_dir(self, dir_name: str) -> 'Directory': #type: ignore
        if dir_name == "..":
            return self.getParent()
        if dir_name == "/": #poor way to handle first instruction but works
            return self
        for item in self.contents:
            if item.getName() == dir_name and type(item) == Directory:
                return item

# Files are types of FileSystems of known size and no children          
class File(FileSystem):
    def __init__(self, name, size=0) -> None:
        super().__init__(name)
        self.size = size
        
    def setSize(self, size: int) -> None:
        self.size = size
        
    def getSize(self) -> int:
        return self.size

# Utility class that builds a filesystem given an input rile
class FileSystemBuilder:
    def __init__(self, root_name = "/") -> None:
        self.currentDir: Directory =  Directory(root_name)
        self.root: Directory = self.currentDir
    
    def _add_dir(self, name):
        self.currentDir.addItem(Directory(name))
    
    def _add_file(self, size, name):
        self.currentDir.addItem(File(name, size))
        
    def _interpret_line(self, line: str, line_number):
        try:
            parsed_line: list = line.split(" ")
            # first manage user input lines
            if parsed_line[0] == "$":
                if parsed_line[1] == "ls":
                    return
                if parsed_line[1] == "cd":
                    self.currentDir = self.currentDir.change_dir(parsed_line[2])
            # add child nodes for directory contents
            elif parsed_line[0] == 'dir':
                self._add_dir(parsed_line[1])
            else:
                self._add_file(int(parsed_line[0]), parsed_line[1])
        except:
            raise Exception("Invalid instruction on input line %d %s" % (line_number, line))
    
    # only public method, returns the completed directory based on input of commands
    def run(self, filepath: str) -> Directory:
        lineNumber = 0
        for line in open(filepath, 'r'):
            lineNumber +=1
            self._interpret_line(line.rstrip(), lineNumber)
        return self.root 
    
def main():
    fs_builder = FileSystemBuilder()
    directory = fs_builder.run("./advent-of-code/day7/input.txt")
    print(directory.format_tree())
    
    #PART ONE
    small_dirs = list()
    MAX_SIZE = 100000 #determined from problem parameters
    directory.get_dirs_under(MAX_SIZE, small_dirs)
    size = 0
    for dir in small_dirs:
        size += dir.getSize()
        print(dir.getName(), dir.getSize())
    print("The total size of the %d directorys under 100,000 is %d" % (len(small_dirs), size))
    
    #PART TWO
    FS_CAPACITY = 70000000
    UPDATE_SIZE = 30000000
    free_space = FS_CAPACITY - directory.getSize()
    min_remove_size = UPDATE_SIZE - free_space
    large_dirs: list[Directory] = list() 
    directory.get_dirs_over(min_remove_size, large_dirs)
    print(len(large_dirs))
    smallest_possible_dir: Directory = large_dirs[0]
    smallest_possible_dir_size = smallest_possible_dir.getSize()
    for dir in large_dirs:
        size = dir.getSize()
        if size < smallest_possible_dir_size:
            smallest_possible_dir_size = size
            smallest_possible_dir = dir
    print("DIR %s with size %d is the smallest directory to remove for the update" % 
          (smallest_possible_dir.getName(), smallest_possible_dir_size))

main()