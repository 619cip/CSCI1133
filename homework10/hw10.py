import math
import random

def cookie_order(cookies):
    '''
    Purpose:
        Give the amount of boxes needed for the amount of cookies given
    Parameter(s):
        cookies : The number of each cookies (dict)
    Return Value:
        Return a dictionary containing cookie_name : amount_of_boxes (dict)
    '''
    cookie_boxes = {}
    for k,v in cookies.items():
        cookie_boxes[k] = math.ceil(v / 30)
    return cookie_boxes

def phonebook(office_name, office_phone):
    '''
    Purpose:
        Point the professor name to their phone number
    Parameter(s):
        office_name : A dict containing Room # : Professor Name (dict)
        office_phone : A dict containing Room # : Phone Number (dict)
    Return Value:
        A dictionary containing Professor Name : Phone Number (dict)
    '''
    office_name_number = {}
    for k,v in office_name.items():
        if k not in office_phone:
            continue
        office_name_number[v] = office_phone[k]
    return office_name_number

def follows(text):
    '''
    Purpose: Gets pairs of adjacent words in a string of text
    Parameters:
        text: sample text to get the adjacent words from (str)
    Return Value:
        A nested dictionary with all pairs of adjacent words.
        The keys in the outer dictionary are the first word in
        each pair from the text, and the values are inner dictionaries
        containing each word that follows that one as keys, and a 
        count of how many times that pair occurs as values (dict)
    '''
    words = text.split()
    pairs = {}
    for i in range(len(words)-1):
        first = words[i]
        second = words[i+1]
        pairs[first] = pairs.get(first, {})
        pairs[first][second] = 1 + pairs[first].get(second, 0)
    return pairs

def random_text(source_file, num_words):
    '''
    Purpose:
        Returns random text with a count of num_words with an
        algorithm that chooses words that are connected to
        each other in the source_file.
    Parameter(s):
        source_file : The path of the file
        num_words : The limit amount of words
    Return Value:
        A string containing num_words amount of words
        with each word being random.
    '''
    res = ''

    str_file = ''
    fp = open(source_file)
    for line in fp:
        str_file += line.strip('\n') + ' '
    fp.close()
    
    def get_freq_num(_dict):
        '''
        Purpose:
            Gets the total sum of values given a dictionary
        Parameter(s):
            _dict : A frequency table (dict)
        Return Value:
            Returns the total sum of dict.values()
        '''
        res = 0
        for v in _dict.values():
            res += v
        return res

    def get_freq_list(pairs):
        '''
        Purpose:
            Converts a frequency table into a frequency list
        Parameter(s):
            pairs : A frequency table (dict)
        Return Value:
            A list containing the amount of elements listed
            in the dictionary. (list)
        '''
        res = []
        for k,v in pairs.items():
            # Get the frequency of our key if our value is a dict
            # Assign v to this frequency.
            if type(v) is dict:
                v = get_freq_num(v)
            for _ in range(v):
                res.append(k)
        return res

    pairs = follows(str_file)
    choices = pairs
    # Loop num_words times (each iteration is +1 word)
    for _ in range(num_words):
        # Convert the frequency table to a frequency list
        # {'a':3, 'b':2, 'c':1} --> ['a', 'a', 'a', 'b', 'b', 'c']
        freq_list = get_freq_list(choices)
        
        # Take a random word from a list of choices
        random_choice = random.choice(freq_list)
        # Add our random choice to our result
        res += random_choice + ' '
        # Have our list of choices be our previous random choice
        # This follows word A -> word B
        choices = pairs[random_choice]
    return res
    


# if __name__ == '__main__':
#     print(cookie_order({'thin mints': 97})) #{'thin mints': 4}
#     print(cookie_order({'thin mints': 34, 'caramel delites': 71,
#                         'shortbread': 60, 'peanut butter': 0}))
#     # {'thin mints': 2, 'caramel delites': 3,
#     #  'shortbread': 2,  'peanut butter': 0}

#     print(cookie_order({})) #{}

# if __name__ == '__main__':
#     print()
#     print(phonebook({'85':'Victoria', '213':'Volkan', '192C':'Mats'},
#              {'192C':'625-2068', '85':'625-3543', '211':'626-1284'}))
#     # {'Victoria': '625-3543', 'Mats': '625-2068'}

#     print(phonebook({'354':'Scot', '355':'Anar', '112A':'Rina'},
#                     {'112A':'625-9835', '512':'626-9137',
#                      '355':'624-5224', '354':'625-5507'}))
#     # {'Scot': '625-5507', 'Anar': '624-5224', 'Rina': '625-9835'}

#     print(phonebook({'4-192':'Dania', '4-192N':'Faith'},
#                     {'4-192L':'624-8311', '4-192D':'626-8020'}))
#     # {}

# if __name__ == '__main__':
#     print()
#     print(follows('what is that there'))
#     # {'what': {'is': 1}, 'is': {'that': 1}, 'that': {'there': 1}}

#     print(follows('one fish two fish red fish blue fish blue'))
#     #{'one': {'fish': 1}, 'fish': {'two': 1, 'red': 1, 'blue': 2},
#     # 'two': {'fish': 1}, 'red': {'fish': 1}, 'blue': {'fish': 1}}

#     print(follows('a b c b a c a d e b a'))
#     #{'a': {'b': 1, 'c': 1, 'd': 1}, 'b': {'c': 1, 'a': 2},
#     # 'c': {'b': 1, 'a': 1}, 'd': {'e': 1}, 'e': {'b': 1}}

#     print(follows('That sam-i-am, that sam-i-am, I do not like '
#                   'that sam-i-am. Do you like green eggs and ham? '
#                   'I do not like them sam-i-am.'))
#     #{'That': {'sam-i-am,': 1}, 'sam-i-am,': {'that': 1, 'I': 1},
#     # 'that': {'sam-i-am,': 1, 'sam-i-am.': 1}, 'I': {'do': 2},
#     # 'do': {'not': 2}, 'not': {'like': 2},
#     # 'like': {'that': 1, 'green': 1, 'them': 1},
#     # 'sam-i-am.': {'Do': 1}, 'Do': {'you': 1}, 'you': {'like': 1},
#     # 'green': {'eggs': 1}, 'eggs': {'and': 1}, 'and': {'ham?': 1},
#     # 'ham?': {'I': 1}, 'them': {'sam-i-am.': 1}}

# if __name__ == '__main__':
#     print()
#     print(random_text('homework10/hw10files/short3.txt', 10))
    
#     print()
#     print(random_text('homework10/hw10files/hamlet.txt', 20))
    
#     print()
#     print(random_text('homework10/hw10files/alice.txt', 30))
