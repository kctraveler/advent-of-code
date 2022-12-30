# Things practiced in this challenge include class methods, map, zip, all
class Forest:
    def __init__(self) -> None:
        self.rows:list[list[int]] = list()
    
    # used by the builder to add one row at a time
    def add_row_trees(self, row:list[int]):
        self.rows.append(row)
    
    # part 1, determine if a tree is visible
    def _is_visible(self, x:int, y:int) -> bool:
        visible = False
        height = self.rows[y][x]
        transposed_rows = list(map(list, zip(*self.rows)))
        if all(h < height for h in self.rows[y][0:x]) or \
            all(h <height for h in self.rows[y][x+1:]) or \
            all(h< height for h in transposed_rows[x][0:y]) or \
            all(h < height for h in transposed_rows[x][y+1:]):
                visible = True         
        return visible
    
    # part 1 iterate through all trees to determine if it is visible
    def count_visible(self) -> int:
        num_visible = 0
        for y in range(len(self.rows)):
            for x in range(len(self.rows[y])):
                if self._is_visible(x, y):
                    num_visible += 1
        return num_visible
    
    # used in part 2 to count number of trees viewable in a single direction
    def _count_trees_in_view(self, tree_height:int, view:list[int]):
        num_viewable = 0
        for tree in view:
            num_viewable += 1
            if tree >= tree_height:
                break
        return num_viewable
        
    # used for part 2 to calculate the scenic score of a tree
    def _scenic_score(self, x:int, y:int) -> int:
        tree = self.rows[y][x]
        transposed_rows = list(map(list, zip(*self.rows)))
        score = 0
        num_east = self._count_trees_in_view(tree, self.rows[y][:x][::-1])
        num_west = self._count_trees_in_view(tree, self.rows[y][x+1:])
        num_north = self._count_trees_in_view(tree, transposed_rows[x][:y][::-1])
        num_south = self._count_trees_in_view(tree, transposed_rows[x][y+1:])
        score = num_east * num_west * num_north * num_south
        return score
    
    # iterate through all trees to find the most scenic
    def find_most_scenic(self) -> int:
        max_scenic_score = 0
        for y in range(len(self.rows)):
            for x in range(len(self.rows[y])):
                score = self._scenic_score(x,y)
                if score > max_scenic_score:
                    max_scenic_score = score
        return max_scenic_score
                

# practice use of class methods to improve on the builder  
class ForestBuilder:
    @classmethod
    def build(cls, file_path: str) -> Forest:
        forest = Forest()
        for line in open(file_path):
            forest.add_row_trees(cls._create_row(line))
        return forest
    
    @classmethod
    def _create_row(cls, line: str) -> list[int]:
        row = list(map(int, line.rstrip()))
        return row
    
def main():
    forest = ForestBuilder.build("./advent-of-code/day8/input.txt")
    print("Number of visible trees: ",forest.count_visible())
    print("The maximum scenic score is ", forest.find_most_scenic())
    
main()
        