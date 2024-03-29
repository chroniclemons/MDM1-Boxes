from allnets import *
import box_drawer as bd
import turtle
import math
window = turtle.Screen()
def create_grid(grid_width,grid_length, window, draw):        # Creates the template for the roller
    if draw:
        global IMAGE #sorry       
        IMAGE = bd.draw_it(grid_width, grid_length)        
        window.screensize(IMAGE.len + 100, IMAGE.wid + 100)
        window.bgcolor("white")  
    return np.zeros((grid_width, grid_length))

def draw_net(net, grid_x_pos, grid_y_pos , grid, colour, draw):       # Draw a given net at a given position
    for row in range(len(net)):
        grid[ grid_y_pos + row , [x for x in range(grid_x_pos, grid_x_pos + len(net[row]) )] ] += net[row]
    if draw:
        M = 0   
        for y in net[0:len(net)]:
            N = 0
            for x in y:
                N += 1
                if x == 1:
                    IMAGE.colour_square( grid_x_pos + N, grid_y_pos + M, net, colour)
            M += 1
    else:
        return
        


def valid_location(net, grid_x_pos, grid_y_pos, grid):      # Determines if a given net will overlap with a previously placed net
    overlap = False

    for matrix_row in range(len(net)):
        #if grid_x_pos == 1:
         #   print(grid_x_pos,grid_y_pos+matrix_row)

        if overlap == False:

            if (BOARD_WIDTH) - (grid_y_pos) < ( len(net) ):   # Prevent the program checking from executing a net that can't fit on the grid
                overlap = True


            if BOARD_LENGTH - (grid_x_pos) < len(net[matrix_row]):  # Prevent the program checking from executing a net that can't fit on the grid
                overlap = True
                break

            check_overlap = net[matrix_row] + grid[ (grid_y_pos + matrix_row) , # This is the y-coord of where the net will be dropped
                                                    [x for x in range(grid_x_pos, grid_x_pos + len(net[matrix_row]) )] ]    # Range of x-coords that the new net will be dropped to

            for element in check_overlap:

                if element == 0 or element ==  1:  # Each value on the grid should either be filled (elem = 1) or empty (elem = 0)
                    pass    # There is no overlap
                else:
                    overlap = True  # There is an overlap between the nets

    return overlap


def get_efficiency(grid):   # Calculates the percentage of the grid used

    total = 0

    for x in range( BOARD_LENGTH ):
        for y in range( BOARD_WIDTH ):
            if grid[(y,x)] == 1:
                total +=1
    efficiency = 100*total/(BOARD_WIDTH*BOARD_LENGTH)
    print("The efficiency is:", efficiency,end="%")
    print("")
    efficiencies.append(efficiency)


def best_grid(list_of_efficiencies):    # Finds the layouts with the best efficiencies
    best_grids = []
    for i in range( 0, len(list_of_efficiencies)):

        if i == 0:
            max = list_of_efficiencies[0]
            best_grids.append(i+1)

        elif list_of_efficiencies[i] > max:
            best_grids = []
            max = list_of_efficiencies[i]
            best_grids.append(i+1)

        elif list_of_efficiencies[i] == max:
            best_grids.append(i+1)

    return best_grids, max


def main(net, window, draw):
    board = create_grid(BOARD_WIDTH, BOARD_LENGTH, window, draw)
    colours = ['blue', 'red', 'orange','yellow', 'purple','green']
    ctr = 0      #counter to help turtle <3    
    nets_drawn = 0  # Counts the number of
    
    for x in range( 0 , BOARD_LENGTH ):
        for y in range( 0 , BOARD_WIDTH ):

            if x == 0 and y == 0:       # Automatically draw a net at (0,0)
                draw_net(net,0,0,board, colours[ctr & 6], draw)
                ctr += 1
                #print(board)
                #print("")

            else:
                if not valid_location(net, x, y, board):
                    draw_net(net, x, y, board, colours[ctr % 6], draw)
                    nets_drawn += 1
                    ctr += 1
                    #print(board)
                    #print("")
    print(board)
    print("There were", nets_drawn, "nets drawn")
    get_efficiency(board)


BOARD_LENGTH = 20
draw = False
efficiencies = []

def run_computations(all_nets, window, w, draw):
    for i in range(len(all_nets)):  # Prints out the optimised board layouts for each individual net
        print("Computing net",i+1)       
        main(all_nets[i], window, draw)
        if draw:
            IMAGE.draw_grid()
            IMAGE.draw_roll()
            window = turtle.Screen()
            window.screensize(IMAGE.len + 100, IMAGE.wid + 100) 
            IMAGE.save_image(window, i+1, w)
            window.clear()
        else:
            continue
        print("")

for w in range(6,17):
    BOARD_WIDTH = w       
    run_computations(all_nets, window, 16, draw)
    
best_nets , best_efficiency = best_grid(efficiencies)
print("The most efficient layout(s) (",best_efficiency,"% )",":")

for i in best_nets:
    if i % 44 == 0 :
        print("Net 44")
    else:
        print("Net "+ str(i % 44))