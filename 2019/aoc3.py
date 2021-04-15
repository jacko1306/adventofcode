with open('/home/florianjacke/vscode/private/jacko/adventofcode/2019/aoc3.txt') as f:
    wires = f.read().splitlines()

visited = [(0,0)]

def addtovisited(x_old, x_new, y_old, y_new):
    global visited
    

for wire in wires:
    x = 0
    y = 0
    instructions = wire.split(",")
    for instruction in instructions:
        if instruction[0] == "R":
            x_old = x
            x = int(instruction[1])
            for i in range(x_old+1,x+1): 
                visited.append((i,y))
        elif instruction[0] == "L":
            x_old = x
            x = int(instruction[1])
            for i in range(x_old,0,-1): 
                visited.append((i,y))
        elif instruction[0] == "U":
            y_old = y
            y = int(instruction[1])
            for i in range(y_old+1,y+1): 
                visited.append((x,i))
        elif instruction[0] == "D":
            y_old = y
            y = int(instruction[1]) 
            for i in range(y_old,0,-1): 
                visited.append((x,i))
            

print(visited)