import math
import time

def get_next_cells(pos,grid):
    moves = []
    if pos[0]+1<len(grid[0])and grid[pos[0]+1][pos[1]] != 1:
        nextpos = pos[0]+1,pos[1]
        moves.append(nextpos)
    if pos[1]+1<len(grid)and grid[pos[0]][pos[1]+1] != 1:
        nextpos = pos[0],pos[1]+1
        moves.append(nextpos)
    if pos[0]-1>=0 and grid[pos[0]-1][pos[1]] != 1:
        nextpos = pos[0]-1,pos[1]
        moves.append(nextpos)
    if pos[1]-1>=0 and grid[pos[0]][pos[1]-1] != 1:
        nextpos = pos[0],pos[1]-1
        moves.append(nextpos)
    return moves

def coords_to_int(coords,size):
    value = int((coords[0])*size+(coords[1]))
    return value

def start_dijkstra(grid,start,end,return_cost,sleep_time):
    size =  len(grid)
    value_grid = [[math.inf for i in range(0,size)] for j in range(0,size)]

    value_grid[start[0]][start[1]]=0

    visited = []
    stack = []
    value_stack=[]

    value_stack.append(1)
    stack.append(start)

    found_end = False
    prev=[(-1,-1) for i in range(0,size*size)]

    while len(stack)>0 and not found_end:
        min_index = value_stack.index(min(value_stack))
        current_cell = stack[min_index]
        cost = value_stack[min_index]

        stack.pop(min_index)
        value_stack.pop(min_index)

        next_cells = get_next_cells(current_cell, grid)
        for cell in next_cells:
            if cell == end:
                found_end=True
            if cell not in visited:
                if value_grid[current_cell[0]][current_cell[1]] + 1 < value_grid[cell[0]][cell[1]]:
                    value_grid[cell[0]][cell[1]] = value_grid[current_cell[0]][current_cell[1]] + cost
                    stack.append(cell)
                    value_stack.append(1)
                    visited.append(cell)
                    prev[coords_to_int(cell, size)] = current_cell
                    print(cell)
                    yield cell
                    if return_cost:
                        yield value_grid[cell[0]][cell[1]]

        time.sleep(sleep_time)
    path = []

    while current_cell != start:
        path.append(current_cell)
        current_cell = prev[coords_to_int(current_cell, size)]

    if found_end:
        yield path
