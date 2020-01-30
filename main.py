import time
import tkinter.font as font
import threading
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
import Astar as astar
import DFS as dfs
import BFS as bfs
import Dijkstra as dijkstra
import random


class button_handler:
    def __init__(self, widget,x,y):
        self.widget = widget
        self.x= x
        self.y= y
        self.pressed_counter = 0
        self.isStart = False
        self.isEnd = False
    def __call__(self):
        global matrix, start, end



        #Check if button is start or end and button is clicked
        if self.isStart==True:
            self.isStart =False
            start=-1,-1
        if self.isEnd==True:
            self.isEnd = False
            end=-1,-1

        if start[0]==-1 and end[0]==-1: #if start and end are not set
            if self.pressed_counter == 0:
                self.widget.configure(bg='black',text = "")
                self.pressed_counter = self.pressed_counter + 1
                matrix[self.x][self.y] = 1

            elif self.pressed_counter ==1:
                self.widget.configure(bg='red',text = "S")
                self.pressed_counter = self.pressed_counter + 1
                matrix[self.x][self.y] = 2
                start=self.x,self.y
                self.isStart = True
                print("Start:",start)

            elif self.pressed_counter==2:
                self.widget.configure(bg='blue',text = "E")
                self.pressed_counter = self.pressed_counter+1
                matrix[self.x][self.y] = 3
                end=self.x,self.y
                self.isEnd=True
                print("End:",end)
            else:
                self.widget.configure(bg='white',text = "")
                matrix[self.x][self.y] = 0
                self.pressed_counter=0
        elif start[0]!=-1 and end[0]==-1:
            if self.pressed_counter == 0:
                self.widget.configure(bg='black',text = "")
                self.pressed_counter = self.pressed_counter + 2
                matrix[self.x][self.y] = 1

            elif self.pressed_counter==2:
                self.widget.configure(bg='blue',text = "E")
                self.pressed_counter = self.pressed_counter+1
                matrix[self.x][self.y] = 3
                end=self.x,self.y
                self.isEnd = True
                print("End:",end)
            else:
                self.widget.configure(bg='white',text = "")
                matrix[self.x][self.y] = 0
                self.pressed_counter=0
        elif start[0]==-1 and end[0]!=-1:
            if self.pressed_counter == 0:
                self.widget.configure(bg='black',text = "")
                self.pressed_counter = self.pressed_counter + 1
                matrix[self.x][self.y] = 1

            elif self.pressed_counter ==1:
                self.widget.configure(bg='red',text = "S")
                self.pressed_counter = self.pressed_counter + 2
                matrix[self.x][self.y] = 2
                start=self.x,self.y
                self.isStart=True
                print("Start:",start)
            else:
                self.widget.configure(bg='white',text = "")
                matrix[self.x][self.y] = 0
                self.pressed_counter=0
        else:
            if self.pressed_counter == 0:
                self.widget.configure(bg='black',text = "")
                self.pressed_counter = self.pressed_counter + 1
                matrix[self.x][self.y] = 1
            else:
                self.widget.configure(bg='white',text = "")
                matrix[self.x][self.y] = 0
                self.pressed_counter=0


def dijkstra_handler():
    global button_matrix,matrix,start,end
    sc = var_showcost.get()

    t0=time.time()
    for return_value in dijkstra.start_dijkstra(matrix, start, end,sc,float(sleep_input.get())):
        if not sc:
            if len(return_value)==2 and type(return_value[0]) is not tuple:
                print(return_value)
                if return_value!=end and return_value!=start:
                    button_matrix[return_value[0]][return_value[1]].config(bg = GREEN )
            else:
                print("Final path")
                for c in range(0,len(return_value)):
                    button_matrix[return_value[c][0]][return_value[c][1]].config(bg=PURPLE)
        else:
            if type(return_value) is int:
                print("Cost of",last_cell,"is",return_value)
                if last_cell != end and return_value!=start:
                    button_matrix[last_cell[0]][last_cell[1]].config(text=str(return_value),compound="c")
            elif len(return_value)==2 and type(return_value[0]) is not tuple:
                last_cell = return_value
                print(return_value)
                if return_value != end and return_value!=start:
                    button_matrix[return_value[0]][return_value[1]].config(bg=GREEN)
            else:
                print("Final Path")
                for c in range(0,len(return_value)):
                    button_matrix[return_value[c][0]][return_value[c][1]].config(bg=PURPLE)
    t1=time.time()
    settime_label.config(text=str(round(t1 - t0,4)))

def astar_handler():
    global button_matrix, matrix, start, end
    sc = var_showcost.get()
    t0=time.time()
    for return_value in astar.start_astar(matrix, start, end, float(sleep_input.get()),sc):
        if not sc:
            if len(return_value) == 2 and type(return_value[0]) is not tuple:
                print(return_value)
                if return_value != end:
                    button_matrix[return_value[0]][return_value[1]].config(bg=GREEN)
            else:
                print("Final path")
                for c in range(0, len(return_value)):
                    button_matrix[return_value[c][0]][return_value[c][1]].config(bg=PURPLE)
        else:
            if type(return_value) is int:
                print("Cost of", last_cell, "is", return_value)
                if last_cell != end:
                    button_matrix[last_cell[0]][last_cell[1]].config(text=str(return_value), compound="c")
            elif len(return_value) == 2 and type(return_value[0]) is not tuple:
                last_cell = return_value
                print(return_value)
                if return_value != end:
                    button_matrix[return_value[0]][return_value[1]].config(bg=GREEN)
            else:
                print("Final Path")
                for c in range(0, len(return_value)):
                    button_matrix[return_value[c][0]][return_value[c][1]].config(bg=PURPLE)
        t1=time.time()
        settime_label.config(text=str(round(t1 - t0,4)))

def dfs_handler():
    global button_matrix,start,end,matrix

    t0=time.time()
    for cell in dfs.start_dfs(matrix, start, end):
        if len(cell)==2 and type(cell[0]) is not tuple:
            print(cell)
            if cell!=end:
                button_matrix[cell[0]][cell[1]].config(bg = GREEN )
            time.sleep(float(sleep_input.get()))
        else:
            print("test")
            for c in range(1,len(cell)):
                button_matrix[cell[c][0]][cell[c][1]].config(bg=PURPLE)
    t1=time.time()
    settime_label.config(text=str(round(t1 - t0,4)))

def bfs_handler():
    global button_matrix,start,end,matrix
    t0= time.time()
    for cell in bfs.start_bfs(matrix, start, end,float(sleep_input.get())):
        if len(cell)==2 and type(cell[0]) is not tuple:
            print(cell)
            if cell!=end:
                button_matrix[cell[0]][cell[1]].config(bg = GREEN )
        else:
            print("Final path",cell)
            for c in range(0,len(cell)):
                button_matrix[cell[c][0]][cell[c][1]].config(bg=PURPLE)
    t1=time.time()
    settime_label.config(text=str(round(t1 - t0,4)))

def startAlgorithm(algorithm):
    global matrix, start, end

    settime_label.config(text="")
    if start[0] != -1 and end[0]!=-1: # if start and end are set
        if algorithm == "A*":
            print("Astar")
            astar_thread = threading.Thread(target=astar_handler,daemon=True)
            astar_thread.start()
        elif algorithm == "Dijkstra":
            print("Dijkstra")
            dijkstra_thread =threading.Thread(target=dijkstra_handler,daemon=True)
            dijkstra_thread.start()
        elif algorithm == "DFS - any path":
            print("DFS")
            dfs_thread = threading.Thread(target=dfs_handler,daemon=True)
            dfs_thread.start()
        elif algorithm == "BFS":
            print("BFS")
            bfs_thread = threading.Thread(target=bfs_handler,daemon=True)
            bfs_thread.start()

def save_map():
    try:
        global matrix
        size = len(matrix)
        file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if size>0:
            for i in range(0,size):
                for j in range(0,size):
                    if matrix[i][j]!=2 and matrix[i][j] !=3:
                        file.write(str(matrix[i][j]))
                    else:
                        file.write("0")
                file.write("\n")
        file.close()
    except:
        pass

def import_map():
    try:
        restart_Clicked()

        global matrix,button_matrix

        file_name = filedialog.askopenfilename(title = "Select map")

        file = open(file_name,'r')
        lines = file.readlines()

        size= len(lines)
        create_Clicked(size)

        for i in range(0,size):
            line =lines[i]
            line=line[:len(line)-1]
            print(line)
            for j in range(0,len(line)):
                matrix[i][j] = int(line[j])
                if line[j]=="1":
                    button_matrix[i][j].config(bg='black')
    except:
        pass




def start_Clicked():
    clear()
    algorithm = algorithm_selection.get()
    startAlgorithm(algorithm)
    print("Start:" ,start)
    print("End:",end)


def create_Button(x , y,x_size,y_size):
    global button_matrix
    helv = font.Font(family='Helvetica', size=int(x_size/2))
    grid_button = Button(grid_frame,image=pixel,width=x_size,height=y_size,bg='white',compound="c",text="",padx="0",pady="0",font = helv)
    grid_button.configure(command=button_handler(grid_button,x,y))
    grid_button.grid(column=y, row=x)
    button_matrix[x][y] = grid_button

def clear():
    global button_matrix, matrix
    size = len(button_matrix)
    for i in range(0,size):
        for j in range(0,size):
            if matrix[i][j]==0:
                button_matrix[i][j].config(bg="white",text="")

def create_Clicked(size):
    try:
        number_size = size
        x_size = int((WIDTH-number_size*6)/int(number_size))
        y_size =int((HEIGHT-OFFSET-number_size*6)/int(number_size))

        print(number_size,number_size,x_size,y_size)

        global matrix, button_matrix
        matrix = [[0 for i in range(number_size)]for j in range(number_size)]
        button_matrix = [[0 for i in range(number_size)]for j in range(number_size)]

        for i in range(0,number_size):
            for j in range(0,number_size):
                create_Button(i,j,x_size,y_size)


        input_size.config(state='disabled')
        button_create.config(state='disabled')
        random_button.config(state = 'normal')
        button_start.config(state='normal')
        algorithm_selection.config(state='normal')
    except:
        pass

def random_Clicked():
    global matrix, button_matrix
    one_percentage = 30         #PERCENTAGE OF GETTING ONE
    size = int(input_size.get())

    for i in range(0,size):
        for j in range(0,size):
            random_number = random.randrange(0,100)
            if random_number<one_percentage:
                matrix[i][j]=1
                button_matrix[i][j].config(bg="black")
            print(matrix[i][j], end = "")
        print()


def create_gridFrame():
    global grid_frame
    grid_frame= Frame(window, width=WIDTH, height=HEIGHT - OFFSET)
    grid_frame.grid(row=1)

def restart_Clicked():
    global matrix, button_matrix, start, end

    matrix = [[]]
    button_matrix=[[]]
    start = [-1, -1]
    end = [-1, -1]

    grid_frame.destroy()

    input_size.config(state='normal')
    button_create.config(state='normal')
    random_button.config(state='disabled')
    button_start.config(state='disabled')
    algorithm_selection.config(state='disabled')
    create_gridFrame()


WIDTH = 610
HEIGHT = 660
OFFSET=60

GREEN = '#99ff33'
PURPLE = '#9867c5'


matrix = [[]]
button_matrix =[[]]
start=[-1,-1]
end=[-1,-1]


window = Tk()
window.geometry(str(WIDTH)+'x'+str(HEIGHT))
window.title("Algorithms")
window.resizable(0,0)
pixel = PhotoImage(width=1, height=1)

#Selection frame
selection_frame = Frame(window,width = WIDTH,height = OFFSET)
selection_frame.grid(row=0)

# size input
size = Label(selection_frame,text="(Size NxN) N:")
size.grid(column=0,row=0)
input_size=Entry(selection_frame,width=10)
input_size.grid(column=1,row=0)


#Algorithm selection
algorithm_selection = Combobox(selection_frame,state = 'disabled')
algorithm_selection['values'] = ("A*","Dijkstra","BFS","DFS - any path")
algorithm_selection.current(0)  # set the selected item
algorithm_selection.grid(column=3, row=0)

#Create Button
button_create = Button(selection_frame,text='Create',command = lambda : create_Clicked(int(input_size.get())),compound="c")
button_create.grid(column=2,row=0)

#Start Button
button_start = Button(selection_frame,text='Start',command = start_Clicked,state = 'disabled')
button_start.grid(column=6,row=0)

#Restart Button
restart_button = Button(selection_frame,text = "Restart",command=restart_Clicked)
restart_button.grid(column=8,row=0)

#clear button
clear_button  =Button(selection_frame,text="Clear",command=clear)
clear_button.grid(column=7,row=0)

#sleep time
sleep_time = Label(selection_frame,text="Sleep time:")
sleep_time.grid(column=4,row=0)
sleep_input=Entry(selection_frame,width=10)
sleep_input.insert(0,"0.1")
sleep_input.grid(column=5,row=0)


#random button
random_button = Button(selection_frame,text="Random Grid",command = random_Clicked,state = "disabled")
random_button.grid(column=0,row=1)

#Show cost checkbox
var_showcost = BooleanVar()
shows_cost = Checkbutton(selection_frame,text = "Show cost",variable = var_showcost)
shows_cost.grid(column=1,row=1)

#save as button
save_button = Button(selection_frame,text="Export map",command=save_map)
save_button.grid(column=3,row=1)

#Import map
import_button = Button(selection_frame,text= "Import map",command=import_map)
import_button.grid(column=4,row=1)

#Labbel time
time_label = Label(selection_frame,text = "Time:")
time_label.grid(column = 7,row=1)
#label settime
settime_label   =Label(selection_frame,text="")
settime_label.grid(column=8,row=1)

#Grid Frame
grid_frame = Frame(window, width=WIDTH, height=HEIGHT - OFFSET)
grid_frame.grid(row=1)

window.mainloop()