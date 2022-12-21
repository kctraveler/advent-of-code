class FileSystem:
    def __init__(self, name) -> None:
        self.name = name
        self.parent = self
    
    def getParent(self) :
        return self.parent
    
    def setParent(self, parent: "Directory"):
        self.parent = parent
        
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
    
class File(FileSystem):
    def __init__(self, name, size=0) -> None:
        super().__init__(name)
        self.size = size
        
    def setSize(self, size: int) -> None:
        self.size = size
        
    def getSize(self) -> int:
        return self.size
  
      
def buildFileSystem(instruction: str):
    input = instruction.split(" ")
    currentFolder = FileSystem("/")
    if input[0] == "$" :
        if input[1] == "cd":        # Potentially un nest some of the if statements here
            if input[2] == "..":
                currentFolder = currentFolder.getParent()
            else:
                pass
                #TODO need to add lookup options to a directory. 
                #set context folder to dir with value in input[2]
        elif input[1] == "ls":
            pass
            #TODO look at use of potnetial generator to keep calling parse instrutction until another $ is reached.
            
# Look at setting up a generator to handle jumping through the commands after an ls?
# 
        
def main():
    with open('./advent-of-code/day7/input.txt') as f:
        input = f.read()
        input = input.split("\n")
    buildFileSystem(input[0])

main()