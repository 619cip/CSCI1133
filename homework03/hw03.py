import math

# Example functions with documentation strings:
# Don't change these functions.

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle (float/int)
    Return Value:
        The given angle’s measure in radians (float)
    '''
    radians = deg * math.pi / 180
    return radians


def cylinder_info(radius, height):
    '''
    Purpose:
        Computes the surface area of a cylinder in square
        meters, and the volume in cubic meters
    Parameter(s):
        radius: The radius of the cylinder in meters (float)
        height: The height of the cylinder in meters (float)
    Return Value:
        None
    '''
    base_area = math.pi * radius * radius
    circ = math.pi * radius * 2
    side_area = circ * height
    print(f'Surface Area: {base_area*2 + side_area} sq. meters')
    print(f'Volume: {base_area * height} cu. meters')


def solve_for_x(equation):
    '''
    Purpose:
        Solves equations of the form "x + _ = _" where the
        values in the blanks are single-digit integers.
    Parameter(s):
        equation: A string of the format "x + _ = _" (str)
    Return Value:
        The value of x that solves the equation (int)
    '''
    first_blank = int(equation[4])
    second_blank = int(equation[8])
    return second_blank - first_blank



# Part A: Documentation
# Fill out the docstrings for each of the three funtions below.
def celsius_to_fahrenheit(celsius):
    '''
    Purpose: 
        Converts celsius to fahrenheit when given temperature in celsius.
    Parameter(s):
        celsius: Temperature in degrees celsius (float)
    Return Value:
        The converted temperature in fahreinheit (float)
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr


def print_25_stars():
    '''
    Purpose:
        Prints 25 asteriks/stars (5x5)
    Parameter(s):
        None
    Return Value:
        None
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')


def miles_per_gallon(start_mileage, end_mileage, gallons):
    '''
    Purpose:
        Given a start mileage, and end mileage. Finds the total
        distance between the two points to find the mpg (miles per gallon)
    Parameter(s):
        start_mileage: The start mileage of the vehicle (float/int)
        end_mileage: The end mileage of the vehicle (float/int)
        gallons: The amount of gallons (float/int)
    Return Value:
        The final calculated miles per gallon. (float)
    '''
    dist = end_mileage - start_mileage
    return dist / gallons



# Part B: Test Cases
# Copy-paste the if __name__ == '__main__' blocks containing the
# test cases for Part B here, and add your additional test cases to them. 
if __name__ == '__main__':
    print(celsius_to_fahrenheit(12.5))  #Should output 54.5
    print(celsius_to_fahrenheit(0.0))   #Should output 32.0
    print(celsius_to_fahrenheit(5.0))   #Should output 41.0
    print(celsius_to_fahrenheit(10))    #Should output 50.0

    print()  #Empty line to separate tests for different functions

    print(miles_per_gallon(5320.5, 5321.5, 2.5))  #Should output 0.4
    print(miles_per_gallon(0, 1200, 40))          #Should output 30.0
    print(miles_per_gallon(1000, 2000, 5))        #Should output 200.0
    print(miles_per_gallon(0, 10000000, 100))     #Should output 100000.0



# Part C: Course Number Inflation
# Write your plus_one function here
# Be sure to include a documentation string inside the function, and
# paste the if __name__ == '__main__': block after the function,
# and add two more test cases to the end of the block.

def plus_one(course):
    '''
    Purpose:
        Add 1 to the course number and return the course with the course number being + 1
    Parameter(s):
        course: given a course name e.g. CSCI 1133 (str)
    Return Value:
        Returns course name with its number being 1 greater. (str)
    '''
    return course[0:5]+str(int(course[-4:])+1)

if __name__ == '__main__':
    print()
    print(plus_one('CSCI 1133')) # output should be CSCI 1134
    print(plus_one('CSCI 5619')) # output should be CSCI 5620
    print(plus_one('CSCI 1160')) # output should be CSCI 1161
    print(plus_one('CSCI 1161')) # output should be CSCI 1162

# Part D: Projectile Motion
# Write your trajectory function here.
# Be sure to include a documentation string inside the function, 
# paste the if __name__ == '__main__': block after the function.

def trajectory(speed, height, angle):
    '''
    Purpose:
        Calculates the trajectory of an object given the speed/height/angle.
        Prints the x,y velocity and returns the distance along the horizontal plane.
    Parameter(s):
        speed: The speed of the object in m/s (float)
        height: The peak height the object has reached in meters (float)
        angle: The object's direction relative to 0,0 in degrees (float)
    Return Value:
        The distance the object has reached when its horizontal velocity reaches 0 (float)
    '''
    v_x = speed * math.cos(math.radians(angle))
    v_y = speed * math.sin(math.radians(angle))

    time = (v_y + math.sqrt(v_y**2 + 19.6*height)) / 9.8
    dist = v_x * time

    print(f"Horizontal Speed: {v_x}\nVertical Speed: {v_y}\nFlight Time: {time}")
    return dist

if __name__ == '__main__':
	print()
	flight1 = trajectory(19.75, 0, 25.375)
	#Horizontal Speed: 17.844566711220764 m/s
	#Vertical Speed: 8.463683529574565 m/s
	#Flight Time: 1.727282352974401 s
	print(f"Flight 1 Distance: {flight1} m")
	#Flight 1 Distance: 30.82260517676607 m

	print()
	flight2 = trajectory(50, 100, 45)
	#Horizontal Speed: 35.35533905932738 m/s
	#Vertical Speed: 35.35533905932737 m/s
	#Flight Time: 9.389000097570259 s
	print(f"Flight 2 Distance: {flight2} m")
	#Flight 2 Distance: 331.9512818776543 m

	print()
	total = flight1 + flight2
	print(f"Total Distance: {total} m")
	#Total Distance: 362.7738870544204 m

