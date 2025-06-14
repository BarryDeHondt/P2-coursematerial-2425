

def closest(points, target_points):
    return min(points, key=lambda p: ((p[0] - target_points[0])**2 + (p[1] - target_points[1])**2) ** 0.5)