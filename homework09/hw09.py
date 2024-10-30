file_dir = ''

def total_hours(filename):
    '''
    Purpose:
        Gets the total sum of all hours worked for an employee
    Parameter(s):
        filename : The directory/name of the file (str)
    Return Value:
        Returns the sum of all the hours the employee has worked
        for the week.
    '''
    fp = open(f'{file_dir}{filename}')

    total = 0
    for line in fp:
        total+=int(line)
    fp.close()

    return total

def label_days(filename):
    '''
    Purpose:
        Takes hours worked and adds the days in a week
        to correspond to the hours the employee has worked
        This is written to a file named 'labeled_filename'
    Parameter(s):
        filename : The file containing the employee's hours (str)
    Return Value:
        None
    '''
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    data = None
    with open(f'{file_dir}{filename}') as file:
        data = file.readlines()

    with open(f'{file_dir}labeled_{filename}', 'w') as file:
        for i in range(7):
            file.write(f'{days[i]}: {data[i]}')

def stretch_model(fname_in, fname_out):
    '''
    Purpose:
        Stretches a model's Y vertex by a factor of 2 and writes
        it to a file named after a user input.
    Parameter(s):
        fname_in : The directory/name of the file containing vertices/faces (str)
        fname_out : The directory/name of the file that stores the results (str)
    Return Value:
        Returns -1 if encounter a FileNotFoundError or FileExistsError
        Returns the # of vertices found in the given file.
    '''
    faces = []
    vertices = []
    factor = 2

    try:
        with open(f'{file_dir}{fname_in}') as file:
            for line in file:
                if line[0] == 'v':
                    vertices.append(line)
                else:
                    faces.append(line)
    except (FileNotFoundError, FileExistsError):
        return -1

    with open(f'{file_dir}{fname_out}', 'w') as file:
        for data in vertices:
            vertex = data.split()
            vertex[2] = str(float(vertex[2]) * factor)
            file.write(f'{' '.join(vertex)}\n')
        for face in faces:
            file.write(f'{face}')

    return len(vertices)

def count_votes(district, office):
    '''
    Purpose:
        Find the winning candidate for the given office and district.
    Parameter(s):
        district : the csv file name (str)
        office : the specified office needed (str)
    Return Value:
        The winner of the given office and the
        amount of votes received (list)
    '''
    candidates = {} # frequency table
    offices = None
    voting_data = None
    winner, votes = None, 0

    # grab the offices ran and voting data
    with open(f'{file_dir}{district}') as file:
        # python doing the dirty work !!!
        offices = [x for x in file.readline().split(',')]
        offices[-1] = offices[-1].strip('\n')

        ind = offices.index(office)
        voting_data = [line.strip('\n').split(',')[ind] for line in file.readlines()]
    
    # add 1 vote every time name appears
    for name in voting_data:
        candidates[name] = 1 + candidates.get(name,0)
    
    # find candidate with maximum number of votes
    for name, num_votes in candidates.items():
        if num_votes > votes:
            winner = name
            votes = num_votes
    
    return [winner, votes]


if __name__ == '__main__':
    print(total_hours('employee1.txt'))
    print(total_hours('employee2.txt'))
    print(total_hours('employee3.txt'))

if __name__ == '__main__':
    label_days('employee1.txt')
    label_days('employee2.txt')
    label_days('employee3.txt')

if __name__ == '__main__':
    print(stretch_model('missing.obj', 'doesntmatter.obj')) #-1
    print(stretch_model('triforce.obj', 'triforce_stretched.obj')) #9
    print(stretch_model('teapot.obj', 'tall_teapot.obj')) #3644

if __name__ == '__main__':
    print()
    print(count_votes('district_0z.csv', 'Mayor'))
    #['Leslie Knope', 2]

    print(count_votes('district_4b.csv', 'City Question 1'))
    #['YES', 10]

    print(count_votes('district_60b.csv', 'County Commissioner District 4'))
    #['Angela Conley', 49]
