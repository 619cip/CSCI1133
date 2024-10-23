import copy, bmp_edit
import math

#Problem A: Grayscale
def grayscale(img_matrix):
    '''
    Purpose:
      Converts all pixel colors of an image to the average 
      of their RGB values aka the color grey.
    Parameter(s):
      A 3D matrix (list of lists of lists) representing an .bmp image
      Each element of the matrix represents one row of pixels in the image
      Each element of a row represents a single pixel in the image
      Each pixel is represented by a list of three numbers between 0 and 255
      in the order [red, green, blue]
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height):
        for x in range(width):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            red = img_matrix[y][x][0]
            green = img_matrix[y][x][1]
            blue = img_matrix[y][x][2]
            avg = (red+green+blue)//3
            img_matrix[y][x][0] = avg
            img_matrix[y][x][1] = avg
            img_matrix[y][x][2] = avg
    return img_matrix

    
#Problem B: Rotate Quadrants
def rotate_quadrants(img_matrix):
    '''
    Purpose:
      Split the image into four equally sized quadrants, and rotate
      them clockwise to form the output image.
    Input Parameter(s):
      (see grayscale) - plus, it can be assumed the img_matrix will have
      an even number of rows and columns.
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.  
    '''
    #TODO: Fix the logic error in the code
    height = len(img_matrix)  
    width = len(img_matrix[0]) 
    for y in range(height//2):
        for x in range(width//2):
            temp = img_matrix[y][x].copy()
            img_matrix[y][x] = img_matrix[y+height//2][x] # flip quad 1 with quad 3
            img_matrix[y+height//2][x] = img_matrix[y+height//2][x+width//2] # flip quad 3 with quad 4
            img_matrix[y+height//2][x+width//2] = img_matrix[y][x+width//2] # flip quad 4 with quad 2
            img_matrix[y][x+width//2] = temp # flip quad 2 with quad 1
    return img_matrix


#Problem C: Lossy Compression
def lossy(img_matrix):
    '''
    Purpose:
      Sets all color component values in the image matrix to 0, 100, or 200,
      by rounding down to the nearest 100.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    #TODO: Finish this function
    rows = len(img_matrix)
    cols = len(img_matrix[0])

    for r in range(rows):
        for c in range(cols):
            red = img_matrix[r][c][0]
            green = img_matrix[r][c][1]
            blue = img_matrix[r][c][2]

            # Use integer division to truncate RGB values
            img_matrix[r][c][0] = red // 100 * 100
            img_matrix[r][c][1] = green // 100 * 100
            img_matrix[r][c][2] = blue // 100 * 100
    return img_matrix

#Problem D: Zoom
def zoom(img_matrix):
    '''
    Purpose:
      Doubles the size of the upper-left quadrant of the input
      image, so that it takes up the entire output image.
      Each pixel in the upper-left quadrant of the input is copied
      to a 2x2 block of pixels in the output.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    #TODO: Finish this function
    res_matrix = copy.deepcopy(img_matrix)
    rows = len(img_matrix)//2
    cols = len(img_matrix[0])//2

    for r in range(rows):
        for c in range(cols):
            pixel = img_matrix[r][c].copy()

            res_matrix[r*2][c*2] = pixel
            res_matrix[r*2+1][c*2] = pixel
            res_matrix[r*2][c*2+1] = pixel
            res_matrix[r*2+1][c*2+1] = pixel

    return res_matrix
    
                

#Problem E: Your Own Filter
def custom_filter(img_matrix):
    '''
    Purpose:
      Tilt the image 45 degrees
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    # If you were to rotate an image 45 degrees beyond its frame
    # there should be some white space shown (for rectangular images)

    # The magnitude of some point from the center should be the same magnitude when rotated
    # If this magnitude exceeds our frame size, then pixel is not shown.
    # The amount of pixels not shown is directly proportional to the amount of white space in the image

    # In our case, (0,0) is located on the top left
    # due to the nature of arrays. So we must offset everything
    # by getting the (x,y) of the middle point of the image.
  
    def magnitude(pt1, pt2):
        '''
        Purpose:
          Finds the magnitude of two points
        Parameter(s):
          pt1 : A vector (tuple)
          pt2 : A vector (tuple)
        Return Value:
          The distance between two vector points (float)
        '''
        return math.sqrt((pt2[0]-pt1[0])**2 + (pt2[1] - pt1[1])**2)
    
    rows = len(img_matrix)
    cols = len(img_matrix[0])
    origin = (rows//2, cols//2)

    res_matrix = [[[255,255,255] for _ in range(cols)] for _ in range(rows)]

    # to figure our new index of the point, we refer to the angle from the center
    # using a relative coordinate system from a point (0,0) to the positive origin (250,250)
    # we can assume the angle between (x,y) and the origin are consistent at different quadrants
    # tan(θ) = opp / adj --> θ = arctan(opp / adj)
    # Since we know the magnitude is always the same when rotated.
    # We can solve for x and y of our new angle.
    # Then apply the offset origin

    for y in range(rows):
      for x in range(cols):
        pixel = img_matrix[y][x].copy()

        # relative coordinates to origin (middle of image)
        # in this case, our origin can be in the top left quadrant
        rel_x = x - origin[0]
        rel_y = y - origin[1]
        dist = magnitude((x,y), origin)

        # we use atan2 as its between -pi and pi, then shift it 45 degrees
        angle = math.atan2(rel_y, rel_x) + math.radians(45)
        
        # convert relative coordinates to global coordinates
        # apply our offset (adding x -> right) (adding y -> down)
        new_x = int(origin[0] + dist * math.cos(angle))
        new_y = int(origin[1] + dist * math.sin(angle))

        if 0 <= new_y < rows and 0 <= new_x < cols:
          res_matrix[new_y][new_x] = pixel
  
    return res_matrix




if __name__ == '__main__':
  print(grayscale([[[127, 127, 127], [0, 0, 0]],
                  [[255, 255, 0], [50, 128, 255]],
                  [[0, 0, 255], [0, 255, 0]],
                  [[255, 0, 0], [255, 255, 255]]]))
  bmp_edit.transform('dice.bmp', grayscale)
  bmp_edit.transform('cat.bmp', grayscale)
  bmp_edit.transform('connector.bmp', grayscale)

if __name__ == '__main__':
    print(rotate_quadrants([[[127, 127, 127], [0, 0, 0]],
                           [[255, 255, 0], [50, 128, 255]],
                           [[0, 0, 255], [0, 255, 0]],
                           [[255, 0, 0], [255, 255, 255]]]))
    
if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', rotate_quadrants)
    bmp_edit.transform('cat.bmp', rotate_quadrants)
    bmp_edit.transform('connector.bmp', rotate_quadrants)

if __name__ == '__main__':
    print(lossy([[[127, 127, 127], [0, 0, 0]],
    [[255, 255, 0], [50, 128, 255]],
    [[0, 0, 255], [0, 255, 0]],
    [[255, 0, 0], [255, 255, 255]]]))

if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', lossy)
    bmp_edit.transform('cat.bmp', lossy)
    bmp_edit.transform('connector.bmp', lossy)

if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', zoom)
    bmp_edit.transform('cat.bmp', zoom)
    bmp_edit.transform('connector.bmp', zoom)

if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', custom_filter)
    bmp_edit.transform('cat.bmp', custom_filter)
    bmp_edit.transform('connector.bmp', custom_filter)
