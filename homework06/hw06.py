def list_difference(numlist1, numlist2):
    '''
    Purpose: 
        Subtract two integers at indicies 0 to length of list
    Parameter(s):
        numlist1 : a list of numbers (list)
        numlist2 : a list of numbers (list)
    Return Value:
        a list containing numlist1 numbers subtracting numlist2
        numbers at their corresponding index values (list)
    '''
    size = len(numlist1)
    res = []

    for i in range(size):
        res.append(numlist1[i] - numlist2[i])

    return res

def closest(vals):
    '''
    Purpose:
        Find the smallest difference between
        two values given a list.
    Parameter(s):
        vals : A list containing numbers (list)
    Return Value:
        The lowest difference # in the list (float)
    '''
    min = abs(vals[0] - vals[1])
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            if abs((vals[i] - vals[j])) < min:
                min = abs((vals[i] - vals[j]))
    return min

def change_key(notes, up):
    '''
    Purpose:
        A Musical Key Converter
        Shift the key of a note by a listed amount
        of 'up' and return the new notes.
    Parameter(s):
        notes : A list of music notes (list)
        up : The amount of steps that should be shifted (int)
    Return Value:
        A new list of musical notes shifted by # up (list)
    '''
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    threshold = len(scale)
    res = []

    for i in range(len(notes)):
        ind = scale.index(notes[i]) + up
        if abs(ind) >= threshold:
            ind %= threshold
        res.append(scale[ind])
    return res

def avoid_sz(names):
    '''
    Purpose:
        Sort a list of names to set names
        containing 's' or 'z' | 'S' or 'Z'
        at an even index (not zero-based)
    Parameter(s):
        names : A list of names (list)
    Return Value:
        A sorted list if the amount of names
        containing 's' or 'z' can even out
        with the amount of non s/z names. (list)

        If this is not the case
        return an empty list (list)
    '''
    res, has_sz, no_sz = [], [], []
    
    # Seperate the list of names into 2 lists
    # has_sz : contains 's' and 'z'
    # no_sz : contains no 's' or 'z'
    for name in names:
        if 's' in name.lower() or 'z' in name.lower():
            has_sz.append(name)
        else:
            no_sz.append(name)
    
    # Check case if there is 1 more s/z's than non s/z
    if len(has_sz) - len(no_sz) >= 1: 
        print('Impossible: Too many s/z names')
        return res
    
    # Iterate through has_sz as it contains the same # as no_sz
    for i in range(len(has_sz)):
        if no_sz[i] and has_sz[i]:
            res.append(no_sz[i])
            res.append(has_sz[i])

    # Check the edge case if there is more no_sz's
    if len(no_sz) > len(has_sz):
        res += no_sz[len(has_sz):]
    return res



if __name__ == '__main__':
    alist = [5, 6, 7]
    blist = [2, 2, 2]
    print(list_difference(alist, blist)) #[3, 4, 5]
    print(alist) #[5, 6, 7]
    print(blist) #[2, 2, 2]
    print(list_difference([0, 1, 1, 2], [3, 5, 8, 13])) 
    #[-3, -4, -7, -11]
    print(list_difference([], [])) #[]

if __name__ == '__main__':
    print()
    print(closest([6, -9, -7, 4, 1]))  #2
    print(closest([14, -57]))  #71
    print(closest([44, 87, -35, -91, -23, 27, 12]))  #12
    print(closest([7, 423, 937, -966, 762, -889, -961, -72]))  #5

if __name__ == '__main__':
    print()

    print(change_key(['G', 'G', 'D', 'D', 'E', 'E', 'D'], 2))
    #['A', 'A', 'E', 'E', 'F#', 'F#', 'E']

    print(change_key(['A', 'A', 'A', 'F', 'C', 'A', 'F', 'C', 'A'],-4))
    #['F', 'F', 'F', 'C#', 'G#', 'F', 'C#', 'G#', 'F']

    print(change_key(['E', 'E', 'F', 'G', 'G', 'F', 'E', 'D',
                      'C', 'C', 'D', 'E', 'E', 'D', 'D'], 3))
    #['G', 'G', 'G#', 'A#', 'A#', 'G#', 'G', 'F',
    # 'D#', 'D#', 'F', 'G', 'G', 'F', 'F']

    print(change_key(['E', 'F#', 'A', 'F#', 'C#', 'C#', 'B', 'E', 'F#', 
                      'A', 'F#', 'B', 'B', 'A', 'G#', 'F#'], -1987))
    #['A', 'B', 'D', 'B', 'F#', 'F#', 'E', 'A', 'B', 
    # 'D', 'B', 'E', 'E', 'D', 'C#', 'B']

if __name__ == '__main__':
    print()
    print(avoid_sz(['Sam Fountain', 'Andrew LaFortune']))
    #['Andrew LaFortune', 'Sam Fountain']

    print(avoid_sz(['Lucas Flom', 'Emily Welp', 'Akshay Peddi']))
    #Impossible: Too many s/z names
    #[]

    print(avoid_sz(['Jessica Thorne', 'Manan Mrig', 'Elijha Gordon',
                    'Daniel Bins', 'Abdul Abdullahi', 'Chris Park',
                    'Nathan Stearley', 'Aishwarya Belhe']))
    #Impossible: Too many s/z names
    #[]


    #Note: There are many valid orders for the remaining test cases,
    #so long as the names containing s/z end up at odd indexes

    print(avoid_sz(['Andy Exley', 'Nao O', 'Euna Ka', 'John Bartucz']))
    #['Andy Exley', 'John Bartucz', 'Nao O', 'Euna Ka']
    
    print(avoid_sz(['Ashlyn Pietski', 'Nathan Anye', 'William Chance',
                    'Demond Counce', 'David Nguyen', 'Ahmed Shahkhan',
                    'Mitch Gansemer', 'Nakul Suresh']))
    #['Nathan Anye', 'Ashlyn Pietski', 'William Chance',
    # 'Ahmed Shahkhan', 'Demond Counce', 'Mitch Gansemer',
    # 'David Nguyen', 'Nakul Suresh']

    print(avoid_sz(['Fatima Browne', 'Pranav Tadi', 'Rijul Mahajan',
                    'Audrey Gasser', 'Kush Patel', 'Athreyi Badithela',
                    'Eric Fredericks', 'Jennie Lim', 'Adrika Dasgupta',
                    'Tia Truong', 'Abdul Rahman Al Hosni']))
    #['Fatima Browne', 'Audrey Gasser', 'Pranav Tadi',
    # 'Kush Patel', 'Rijul Mahajan', 'Eric Fredericks',
    # 'Athreyi Badithela', 'Adrika Dasgupta', 'Jennie Lim',
    # 'Abdul Rahman Al Hosni', 'Tia Truong']