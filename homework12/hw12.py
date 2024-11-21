class Complex:
    '''
    Purpose: (What does an object of this class represent?)
        Represent a complex number
    Instance variables: 
        real : A real number (float)
        imag : An imaginary number i (float)
    Methods:
        Getter and Setter methods to alternate real/imag numbers
        Overrides str/add/mul/eq method to ensure valid
        real-imaginary number addition/representation/multiplication/logic
    '''

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag
    
    def set_real(self, real):
        self.real = real
    
    def set_imag(self, imag):
        self.imag = imag

    def __str__(self):
        return f'{self.real} + {self.imag}i'
    
    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)
    
    def __mul__(self, other):
        real_prod = self.real*other.real
        imag_prod = self.imag*other.imag
        ri_prod = self.real*other.imag
        ri_prod2 = self.imag*other.real
        return Complex(real_prod-imag_prod, ri_prod+ri_prod2)

    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        return False

class Decision:
    '''
    Purpose:
        A decision holding multiple different options which
        outputs different results depending on the user input
    Instance variables:
        prompt : Holds the main prompt of the story (str)
        options : Holds all the possible options for the instance (list)
        results : Holds all the possible results for the instance (list)
    Methods: (What methods does this class have, and what does each do in a few words?)
        add_option : Adds an option and result to the instance
        run : Prompts the user to pick and choose a decision and returns the result
              from the given input.
    '''

    def __init__(self, prompt):
        self.prompt = prompt
        self.options = []
        self.results = []

    def add_option(self, option, result):
        self.options.append(option)
        self.results.append(result)

    def run(self):
        if not self.options:
            return 'No options available'
        print(f'\n{self.prompt}\n')
        for i in range(len(self.options)):
            print(f'{i}. {self.options[i]}')

        ind = input(f'Enter an input between 0 and {len(self.options)-1} ')
        res = self.results[int(ind)]

        if isinstance(res, str):
            return res
        return res.run()

class Flowchart:
    '''
    Purpose: 
        Converts a preset file to a story problem of any size and
        plays it when start method is called.
    Instance variables:
        decisions : Represents the amount of decision objects there are in
                    the story (list)
    Methods: (What methods does this class have, and what does each do in a few words?)
        start : Starts the story by running the decision
    '''

    def __init__(self, filename):
        self.decisions = []

        fp = open(filename)
        for line in fp:
            
            line = line.strip()
            line_arr = line.split(',')
            story_type = line_arr.pop(0)
            index = line_arr.pop(0)

            if 'Decision' == story_type:
                self.decisions.append(Decision(line_arr[0]))
            elif 'Ending' == story_type:
                instance = self.decisions[int(index)]
                instance.add_option(line_arr[0], line_arr[1])
            elif 'Path' == story_type:
                instance = self.decisions[int(index)]
                instance2 = self.decisions[int(line_arr[1])]
                instance.add_option(line_arr[0], instance2)

        fp.close()

    def start(self):
        return self.decisions[0].run()
