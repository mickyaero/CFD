from __future__ import print_function

#grid size = (m+1, m+1)
print("Enter the size of the grid")

size = input() #it has to be greater than or equal to 2
grid_pts = [[0 for x in range(size)] for y in range(size)]

""" The boundary conditions are the temperature at the upper surface = t1, lower surface = t2, at the right surface it is t3, at the left surface it is t4"""
print("Enter the upper surface temp")
t1 = input()

print("Enter the lower surface temp")
t2 = input()
print("Enter the right surface temp")
t3 = input()
print("Enter the left surface temp")
t4 = input()


error_m = []

print("enter the epsilon_c")
epsilon_c = input()

for i in range(size-2):
    for j in range(size-2):
        grid_pts[i+1][j+1] = 0.0

for i in range(size):
    grid_pts[0][i] = t1          #upper surface
    grid_pts[size-1][i] = t2     #lower surface
    grid_pts[i][0] = t3          #right surface
    grid_pts[i][size-1] = t4     #left surface

"""n is the iteration number """
print("Enter the no of iterations")
n = input()

grid_pts_dummy = [[0 for x in range(size)] for y in range(size)]

#grid_pts_dummy = grid_pts   ....check this statement..why does this produces errors

for i3 in range(n):
    c = 0.0
    """ This is what happens in a particular iteration"""
    for i in range(1,size-2):
        for j in range(1,size-2):
            grid_pts_dummy[i][j] = (grid_pts[i-1][j] + grid_pts[i+1][j] + grid_pts[i][j-1] +grid_pts[i][j+1])/4
            

    for i1 in range(1,size-2):
        for j1 in range(1,size-2):

	    c = c + (grid_pts_dummy[i1][j1] - grid_pts[i1][j1]) ** 2
            
            grid_pts[i1][j1] = grid_pts_dummy[i1][j1]
    
    c = c ** 0.5

    error_m.append(c)
   # print(c)


print(error_m)  
""" Printing the final temperature grid"""
"""
for i in range(size):
    print("\n")	   
    for j in range(size):
        print(grid_pts[i][j]," ", end="") 

"""



