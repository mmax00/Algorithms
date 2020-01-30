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

def start_bfs(grid,start,end,sleep_time):
    stack = []
    stack.append(start)

    grid_size = len(grid)

    current_cell=(-1,-1) #cell not set yet
    found_end = False

    visited =[]
    visited.append(start)
    prev=[(-1,-1) for i in range(0,grid_size*grid_size)]

    while len(stack)>0 and not found_end:
        current_cell = stack[0]
        stack.pop(0)

        next_cells = get_next_cells(current_cell,grid)
        for cell in next_cells:
            if cell == end:
                found_end=True
            if cell not in visited:
                stack.append(cell)
                visited.append(cell)
                prev[coords_to_int(cell,grid_size)] = current_cell
                yield cell

        time.sleep(sleep_time)

    path = []

    while current_cell!=start:
        path.append(current_cell)
        current_cell = prev[coords_to_int(current_cell,grid_size)]

    if found_end:
        yield path


