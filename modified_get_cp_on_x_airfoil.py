from __future__ import division

#I MUST HAVE THE VALUE AT X = 0 AND X = 1 OF TARGET CP DISTRIBUTION
#Airfoil lower and upper must vary from 0 to 1, not necessarily including 0 and 1 but between 0 and 1
#Cp upper and lower x coordinate  must vary between 0 and 1 and 0 and 1 must be present there otherwise inlude them

import matplotlib.pyplot as plt
def get_cp_on_x(cp_x, airfoil_x):
#cp_x is a 2d array- consisting of cp and its x coordinates, whereas airfoil is a 1d array consisting of starting airfoil x coordinates
    tell = 0
    while cp_x[1][tell]!=0:
        tell = tell+1

    upper_tar = [[0 for i in range(tell+1)] for y in range(2)]
    lower_tar = [[0 for i in range(len(cp_x[0])-tell)] for y in range(2)]
    

    for i in range(tell+1): 
        upper_tar[0][i] = cp_x[0][i]
        upper_tar[1][i] = cp_x[1][i]

    
    for i in range(len(cp_x[0])-tell):
        lower_tar[0][i] = cp_x[0][tell+i]
        lower_tar[1][i] = cp_x[1][tell+i]

    

    tel3 = 0
    while airfoil_x[tel3]!=0:
        tel3 = tel3+1
    airfoil_x_upper = [0 for i in range(tel3+1)]
    airfoil_x_lower = [0 for i in range(len(airfoil_x)-tel3)]
    for i in range(tel3+1): 
        airfoil_x_upper[i] = airfoil_x[i]
        

    
    for i in range(len(airfoil_x)-tel3):
        airfoil_x_lower[i] = airfoil_x[tel3+i]
        


    len_airfoil_lower = len(airfoil_x_lower)
    len_airfoil_upper = len(airfoil_x_upper)
    len_lower_x = len(lower_tar[1])
    len_upper_x = len(upper_tar[1])
    cp_airfoil_upper = []
    cp_airfoil_lower = []
    for i in range(len_airfoil_lower):
        for j in range(1,len_lower_x):
            if airfoil_x_lower[i] <= lower_tar[1][j] and airfoil_x_lower[i] >= lower_tar[1][j-1]:
                data = lower_tar[0][j] + (airfoil_x_lower[i]-lower_tar[1][j]) * (lower_tar[0][j]-lower_tar[0][j-1])/(lower_tar[1][j]-lower_tar[1][j-1])
                cp_airfoil_lower.append(data)
                break
    for i in range(len_airfoil_upper):
        for j in range(1,len_upper_x):
            if airfoil_x_upper[i] >= upper_tar[1][j] and airfoil_x_upper[i] <= upper_tar[1][j-1]:
                data = upper_tar[0][j] + (airfoil_x_upper[i]-upper_tar[1][j]) * (upper_tar[0][j]-upper_tar[0][j-1])/(upper_tar[1][j]-upper_tar[1][j-1])
                cp_airfoil_upper.append(data)
                break
    del cp_airfoil_upper[-1]

    final = cp_airfoil_upper + cp_airfoil_lower
    return final


cp_x=[(0.1, 0.3, 0.5, 0.8, 0.6, 0.25, 0.34, 0.65, 0.2, 0.8, 0.9, 0.4),(1, 0.9, 0.7, 0.6, 0.4, 0.1, 0, 0.2, 0.4, 0.7, 0.9, 1)]  


airfoil_x = [1, 0.98, 0.95, 0.8, 0.74, 0.75, 0.7, 0.68, 0.5, 0.45, 0.2, 0.1, 0, 0.1 ,0.25, 0.26, 0.32, 0.34, 0.5, 0.7, 0.72, 0.85, 0.93, 1]


letsc = get_cp_on_x(cp_x, airfoil_x)
print len(letsc)

plt.plot(cp_x[1], cp_x[0])
plt.plot(airfoil_x, letsc)

plt.show()
