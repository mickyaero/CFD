import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt


airfoil = [[0]*1001 for x in range(2)]
ix = [0 for i in range(1000)]
iy = [0 for i in range(1000)]
"""
print(airfoil[1])
airfoil[0][n] represents x coordinate of the nth point
airfoil[1][n] represents y coordinate of the nth point
"""


ix = np.genfromtxt('xcoordinate.csv', delimiter = ',')
iy = np.genfromtxt('ycoordinate.csv', delimiter = ',')

for i in range(1000):
    airfoil[0][i] = ix[i]
    airfoil[1][i] = iy[i]

airfoil[0][1000] = 0
airfoil[1][1000] = 0
"""
print(airfoil)
"""

"""
plt.plot(airfoil[0],airfoil[1])
plt.show()

"""

"""
Creating the mesh

"""
"""
maybe the control point
"""
control_parameter = 150

"""
West and East sides 
For the west and the east side, there will be a common line, emanating from the leading edge i.e airfoil[][501] and will intersect
the square boundary(North BC). It depends on the ( LE-1)th point, (LE+1)th point and the (LE)th point on the airfoil.
(LE-1) = airfoil[][999]
(LE) = airfoil[][0]
(LE+1) = airfoil[][1]

"""

"""
Finding out the point of intersection with the square

"""

"""
Calculating the slope of the line

"""


m_1 = (airfoil[1][1] - airfoil[1][0]) / (airfoil[0][1] - airfoil[0][0])

m_2 = (airfoil[1][999] - airfoil[1][0]) / (airfoil[0][999] - airfoil[0][0])

if (m_1 + m_2) == 0:
    m_3 = 0

else:
    m_3 = ( m_1*m_2 -1 + ((m_1 ** 2 + 1) ** 0.5) * ((m_2 ** 2 + 1) ** 0.5)) / (m_1 + m_2)

"""
print(m_3)

"""

if m_3 < 0.75:
   q_x = -2
   q_y = m_3 * q_x
   q_y = float("{0:.1f}".format(q_y))
   c = 1
else:
   q_y =  -1.5
   q_x = q_y / m_3
   q_x = float("{0:.1f}".format(q_x))
   c = 0
"""
print(q_x)
print(q_y)

"""

"""
creating the  sides of the rectangle

"""

if c == 1:
   """ left side"""
   lower = (q_y +1.5)*50
   lower = int(lower)
   upper = 150 - lower
  
   lower_points =[[0]*lower for i in range(2)]
   upper_points =[[0]*upper for i in range(2)]

   for i in range(lower):
       lower_points[0][i] = -2
       lower_points[1][i] = -1.5 + (i) * (q_y + 1.5)/lower

   for i in range(upper):
       upper_points[0][i] = -2
       upper_points[1][i] = q_y + i * (q_y + 1.5)/upper
   """ left side end"""

   """upper side start"""

   right = [[0]*350 for i in range(2)]
   for i in range(350):
       right[0][i] = -2 + i * (5/350)
       right[1][i] = 1.5
   """ upper side end"""

   """ right side start"""
   rig = [[0]*150 for i in range(2)]
   for i in range(150):
       rig[0][i] = 2
       rig[1][i] = 1.5 - i*3/150
   """ right side ends"""
  
   """ bottom side starts"""
   bottom = [[0]*350 for i in range(350)]
   for i in range(350):
       bottom[0][i] = 2 - i*5/350
       bottom[1][i] = -1.5

   """ bottom side ends """
   
   rectangle_boundary = [[0] * 1001 for i in range(2)]
   
   for i in range(upper):
       rectangle_boundary[0][i] = upper_points[0][i]
       rectangle_boundary[1][i]  = upper_points[1][i]

   for i in range(350):
       rectangle_boundary[0][i+upper] = right[0][i]
       rectangle_boundary[1][i+upper] = right[1][i]

   for i in range(150):
       rectangle_boundary[0][i+350+upper] = rig[0][i]
       rectangle_boundary[1][i+350+upper] = rig[1][i]

   for i in range(350):
       rectangle_boundary[0][i+500+upper] = bottom[0][i]
       rectangle_boundary[1][i+500+upper] = bottom[1][i]

   for i in range(lower):
       rectangle_boundary[0][i+850+upper] = lower_points[0][i]
       rectangle_boundary[1][i+850+upper] = lower_points[1][i]
   
   rectangle_boundary[0][1000] = rectangle_boundary[0][0]
   rectangle_boundary[1][1000] = rectangle_boundary[1][1]
    


if c == 0:
   """bottom  starts """
   bottom_right = (2-q_x)*70
   bottom_right = int(bottom_right)
   bottom_left = 350 - bottom_right
  
   right_points =[[0]*bottom_right for i in range(2)]
   left_points =[[0]*bottom_left for i in range(2)]

   for i in range(bottom_right):
       right_points[0][i] = 2 - i * (2-q_x)/bottom_right
       right_points[1][i] = -1.5 

   for i in range(bottom_left):
       left_points[0][i] = q_x - i*(2-q_x)/bottom_left
       left_points[1][i] = -1.5
   """ bottom side ends"""
    
   """ left side starts"""
   lef = [[0]*150 for i in range(2)]
   for i in range(150):
       lef[0][i] = -2
       lef[1][i] = -1.5 + i*3/150
   """ left side ends"""
    
   """upper side start"""

   right1 = [[0]*350 for i in range(2)]
   for i in range(350):
       right1[0][i] = -2 + i * (5/350)
       right1[1][i] = 1.5
   """ upper side end"""

   """ right side starts"""
      
   righhhh = [[0]*150 for i in range(2)]
   for i in range(150):
       righhh[0][i] = 2
       righhh[1][i] = 1.5 - i*3/150
  
   """ right side ends """    

   rectangle_boundary = [[0] * 1001 for i in range(2)]

   for i in range(bottom_left):
       rectangle_boundary[0][i] = left_points[0][i]
       rectangle_boundary[1][i]  = left_points[1][i]

   for i in range(150):
       rectangle_boundary[0][i+bottom_left] = lef[0][i]
       rectangle_boundary[1][i+bottom_left] = lef[1][i]

   for i in range(350):
       rectangle_boundary[0][i+bottom_left+150] = right1[0][i]
       rectangle_boundary[1][i+bottom_left+150] = right1[1][i]

   for i in range(150):
       rectangle_boundary[0][i+500+bottom_left] = righhh[0][i]
       rectangle_boundary[1][i+500+bottom_left] = righhh[1][i]

   for i in range(bottom_right):
       rectangle_boundary[0][i+650+bottom_left] = right_points[0][i]
       rectangle_boundary[1][i+650+bottom_left] = right_points[1][i]

   rectangle_boundary[0][1000] = rectangle_boundary[0][0]
   rectangle_boundary[1][1000] = rectangle_boundary[1][1]


"""  
plt.plot(rectangle_boundary[0], rectangle_boundary[1])
plt.show()

"""   

boundary_line = [[0]*control_parameter for i in range(2)]
boundary_line[0][0] = 0
boundary_line[1][0] = 0
for i in range(control_parameter-1):
    boundary_line[0][i+1] = (3000 ** ((i+1)/(control_parameter-1)))/3000 * q_x
    boundary_line[1][i+1] = (3000 ** ((i+1)/(control_parameter-1)))/3000 * q_y


"""
plt.plot(boundary_line[0], boundary_line[1])
plt.show()
"""


    
    
































