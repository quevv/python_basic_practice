import math

def calculate_euclidean_distance_between_points(points):
    if len(points) < 2:
        raise ValueError("The function requires at least two points.")
    
    else: return sum(
        math.sqrt(
            (points[i+1][0] - points[i][0])**2 + 
            (points[i+1][1] - points[i][1])**2) 
        for i in range(len(points) - 1))

print(calculate_euclidean_distance_between_points([(0, 0), (3, 4), (0, 0)]))
print(calculate_euclidean_distance_between_points([(0, 0), (3, 4), (-1, -1)]))