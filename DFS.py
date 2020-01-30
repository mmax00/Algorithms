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


def start_dfs(grid,start,end):

    visited_cells =[] #keeps track of visited cells
    stack = []  #keeps track of cells
    path =[]    #final path
    current_cell = start
    stack.append(current_cell)
    num_of_visited_cells =0

    while current_cell != end:
        current_cell_has_new_cells =False
        visited_cells.append(current_cell) #add current cell to visited
        next_cells = get_next_cells(current_cell,grid) #get next cell to visit

        for cell in next_cells:
            if cell not in visited_cells:
                current_cell_has_new_cells = True
        if not current_cell_has_new_cells:
            stack.pop(num_of_visited_cells)                        #pop the last cell
            num_of_visited_cells=num_of_visited_cells-1
        else:
            for cell in next_cells:                                    #get next cell
                if cell not in visited_cells:
                    stack.append(cell)
                    yield cell
                    num_of_visited_cells=num_of_visited_cells+1
                    break

        if len(stack)==0:
            return

        current_cell = stack[num_of_visited_cells]

    for cell in stack:
        if cell in visited_cells:
            path.append(cell)
    yield path

