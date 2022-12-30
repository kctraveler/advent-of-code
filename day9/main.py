def move_rope(direction:str, spaces:int):
    pass

def determine_range(filepath:str):
    current_pos:list[int] = [0, 0]
    max_x = min_x =  max_y = min_y = 0
    for line in open(filepath):
        instruction = line.rstrip().split(" ")
        direction, num_spaces = instruction[0], int(instruction[1])
        if direction == 'U':
            current_pos[1] += num_spaces
            if current_pos[1] > max_y:
                max_y = current_pos[1]
        elif direction == "D":
            current_pos[1] -= num_spaces
            if current_pos[1] < min_y:
                min_y = current_pos[1]
        elif direction == "L":
            current_pos[0] -= num_spaces
            if current_pos[0] < min_x:
                min_x = current_pos[0]
        elif direction == "R":
            current_pos[0] += num_spaces
            if current_pos[0] > max_x:
                max_x = current_pos[0]
    print("Width: %d\tHeight: %d" % (max_x - min_x, max_y - min_y))
            
    
def main() -> None:
    filepath = "./advent-of-code/day9/input.txt"
    determine_range(filepath)
    # for line in open(filepath):
    #     instruction =  line.rstrip().split(" ")
    #     print(instruction)

main()
    