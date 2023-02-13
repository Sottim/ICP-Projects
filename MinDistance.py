# Extra_Credit Assignment: Santosh Adhikari
# FIND THE MINIMUM DISTANCE B/W TWO POINTS IN A GRAPH

import math 

def distance_Calc(P1, P2):   # assertion : Using the distance formula calculates the distance between two points P1 and P2
    dist_Formula = (pow(P2[1] - P1[1], 2 ) + pow(P2[0] - P1[0], 2)) #use inbuilt pow function to implement distance formula.
    distance = math.sqrt(dist_Formula)  
    return distance

def bruteForce(Point):   # assertion : Brute_Force is invoked everytime the last 3 points are left and finds the minimum distance.
    closest_dist = float("inf")    
    p1, p2 = None, None  
    L = len(Point)             
    for i in range (L):
        for j in range(i+1, L):
            dis = distance_Calc(Point[i], Point[j])
            if dis < closest_dist:                
                closest_dist = dis
                point1 = Point[i]
                point2 = Point[j]
    return point1, point2, closest_dist       
# Due to one inner loop inside the outer loop the Time Complexity is of the order of O(n ^ 2)
    

def Sort_Recursion(sortX, sortY):
    L = len(sortX)  # To find the length of sortX array.
    if (L <= 3):
        return bruteForce(sortX) # if only three points are left then base case come into play
    else:
        midpoint = sortX[L//2]
        sortX_left = sortX[: L//2]
        sortX_right = sortX[L//2 :]
        sortY_left = []
        sortY_right = []

        for i in sortY:
            #compare the point at i and the midpoint of x at 0, then append to ysorted_left if point is smaller than mid point else append to right.  
            if (i[0] <= midpoint[0]):
                sortY_left.append(i) 
            else: 
                sortY_right.append(i)  
        # Using recursion to find left part of the space. point1_left, point2_left are two points and dist_left is minimum distance in the left part.        
        (p1_left, p2_left, left_distance) = Sort_Recursion(sortX_left, sortY_left)

        # Using recursion to find p1_right and p2_right are two points and right_distance is minimum distace in the right part
        (p1_right, p2_right, right_distance) = Sort_Recursion(sortX_right, sortY_right)

        # assertion : the smallest distance between the left part of the division and right part of the division is a point whoese corrdinate are p1 and p2
        if (left_distance < right_distance):
           (p1, p2, distance) = (p1_left, p2_left, left_distance)
        else :
           (p1, p2, distance) = (p1_right, p2_right, right_distance)
        
        # we are to sort according to the y-coordinate which reduces normal time complexity to (n (log n)^2 to n log n)
        pointin_band = [point for point in sortY if midpoint[0]- distance < point[0] < midpoint[0]+ distance]  # Taking only the points within the length of smallest distance from midpoint  
        Len = len(pointin_band) 
        for i in range (Len):                       
            for j in range(i+1, min(i+7, Len)):        
                small_d = distance(pointin_band[i], pointin_band[j])
                if small_d < distance:
                    print(pointin_band[i], pointin_band[j])
                    (p1, p2, distance) = (pointin_band[i], pointin_band[j], small_d)
        return p1, p2, distance

def Closest_Pairs(Points):  # assertion : Use the inbuilt sort function to sort the x-coordinates of all the point and y-coordinate of all the points
    sortX = sorted(Points, key = lambda point: point[0])  
    sortY = sorted(Points, key = lambda point: point[1])

    return Sort_Recursion(sortX, sortY)
print(Closest_Pairs([[2,3],[10,20],[11,20],[5,10],[12,10],[2,4]]))

# Final Time Complexity : We use the divide and conqure algorithm.
                          # Time complexity for finding close pair + Time Comp. for sorting points along Y coordinate.
                          # O(log n) * O(n) = O)(n log n)

# Proof of Correctness : 
# Base Case : If the total number of points are 3 or less than 3 then Invoke the bruteForce Function.
# Induction Hypothesis : Split the array from the length of Array= L to L div 2
# Induction Step : We use the recursion to continue to split the array to L div 2 to L div 4 and so on.

# By using the divide and conqure algorithm the complexity of our program is highly reduced. 

