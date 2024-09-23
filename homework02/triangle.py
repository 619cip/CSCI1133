x_1 = float(input('Enter x value for point 1: '))
y_1 = float(input('Enter y value for point 1: '))

x_2 = float(input('Enter x value for point 2: '))
y_2 = float(input('Enter y value for point 2: '))

pt_1, pt_2, pt_3 = (x_1, y_1), (x_2, y_2), (0, 0)

print(f'Point 3 set to {pt_3}')

def magnitude(p1, p2):
    return ( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 ) ** 0.5

magn_1, magn_2, magn_3 = magnitude(pt_1, pt_2), magnitude(pt_1, pt_3), magnitude(pt_2, pt_3)
print('Distance between points 1 and 2:', magn_1)
print('Distance between points 1 and 3:', magn_2)
print('Distance between points 2 and 3:', magn_3)
print('Perimeter of triangle:', (magn_1 + magn_2 + magn_3))