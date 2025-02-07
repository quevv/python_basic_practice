import math

def calculate_euclidean_distance_between_2_points(p1, p2):
    # d = căn ((x2 - x1) bình + (y2 - y1) bình)
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print(calculate_euclidean_distance_between_2_points((0, 0), (3, 4)))