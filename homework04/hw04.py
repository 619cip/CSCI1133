def sound(weight):
    '''
        Purpose:
            Check the weight of a dog, if between a certain or below/above a threshold,
            return the appropriate sound of the dog.
        Parameter(s):
            weight: The weight of the dog (float)
        Return value:
            The sound the dog makes based off its weight (str)
    '''
    match weight:
        case weight if weight < 13:
            return 'Yip'
        case weight if 13 <= weight <= 30:
            return 'Ruff'
        case weight if 31 <= weight <= 70:
            return 'Bark'
        case _:
            return 'Boof'
        
def sound2(weight, is_cat):
    '''
        Purpose:
            Determine the sound of the cat, as well as checking if cat or not
            Will return meow if a cat, return dog noise appropriate to weight if not
        Parameter(s):
            weight: The weight of the cat (float)
            is_cat: If the animal is a cat or not (bool)
        Return value:
            Returns the sound of a cat or the sound of a dog (str)
    '''
    if not is_cat:
        return sound(weight)
    return 'Meow'

def three_options(text, optionA, optionB, optionC):
    '''
        Purpose:
            Prompt the user with a text to choose either option A, B, or C.
        Parameter(s):
            text: The prompt the narrator wants to storytell. (str)
            optionA: The option for option A. (str)
            optionB: The option for option B. (str)
            optionC: The option for option C. (str)
        Return value:
            The user's choice made ('A', 'B', 'C') (str)
    '''
    print(f"\n{text}")
    print(f'\nA. {optionA}\nB. {optionB}\nC. {optionC}')
    choice = input('Choose A, B, or C: ')
    while not (choice == 'A' or choice == 'B' or choice == 'C'):
        print('Invalid option, try again')
        choice = input('Choose A, B, or C: ')
    return choice

def adventure():
    '''
        Purpose:
            Creates an Interactive fiction game for the user
        Parameter(s):
            None
        Return value:
            Good ending (True) or bad ending (False) (bool)
    '''
    # Time complexity: O(n) story is fixed/constant, but # of loop ran depends on valid user input.
    # Space complexity: O(1) story is fixed, number of dicts used does not change.

    # Here, each path_ variable store our story prompts to be used in a dict
    # variable path_ includes the index pattern to indicate which part of the story.
    # ~ examples ~
    # path_ac: path_start -> choice A -> choice C
    # path_cb: path_start -> choice C -> choice B
    path_start = {
        'prompt': "A mcdonalds burger man walks up to you asking for change... What should you do?",
        'A': "Lets rob him! (you're a millionare)",
        'B': "Gulp.. lets put him in a mr. beast challenge!",
        'C': "Alright have some change...",
        'end': None
    }
    path_a = {
        'prompt': "You decided to rob him using a gremlin shake you found in your pocket."\
                  '\nThe mcdonalds burger man insists you take all his money...',
        'A': "Yeah nevermind, You're broke!",
        'B': "Haha tonight we'll be rich :D",
        'C': "Nonchalant dreadhead",
        'end': None
    }
    path_aa = {
        'prompt': 'as soon as you called him broke, he whipped out 10 bands and flexed on you...'\
                  '\nbut he forgot that you were robbing him!! (you stole all his money YAY?)',
        'end':True
    }
    path_ab = {
        'prompt': 'you turned out to actually become rich and own the local mcdonalds..? yay?',
        'end':True
    }
    path_ac = {
        'prompt': "As you call him a nonchalant dreadhead. He starts to shake his dreads."\
                  "\nHe chuckles while attempting to rizz you up. What should you do now?",
        'A': "Back off, his nonchalant dreadheadiness has too much aura!",
        'B': "Have a one on one rizz battle with the nonchalant dreadhead.",
        'C': "Wait a minute.. you're in a genjutsu...",
        'end': None
    }
    path_aca = {
        'prompt': 'You decided to back off.. As you back off, burgerman crashed out and you'\
                  '\nwere able to escape from his aura.',
        'end':True
    }
    path_acb = {
        'prompt': "as you attempt to have a rizz battle with the nonchalant dreadhead"\
                  "\nhe conquerored six eyes of unspoken rizz an hour ago which gathered all"\
                  "\nthe local singles within 1 mile, putting you at shame and speechless...",
        'end':False
    }
    path_acc = {
        'prompt': "you figured out that it was all a trick! but a little.. too late?",
        'end':False
    }
    path_b = {
        'prompt': 'as you try to attempt to bring him to a so-called mr. beast challenge'\
                  " he knew you were broke and started calling you 'mr. least'..",
        'end':False
    }
    path_c = {
        'prompt': 'you let him rob you, but at what cost? you decide to go on with life, OR DO YOU?',
        'A':'screw revenge...',
        'B':'I WANT REVENGE (call him a nonchalant dreadhead)',
        'C':'well it is what it is...',
        'end':None
    }
    path_ca = {
        'prompt': "well you lost money and you didn't even get food.. womp womp.",
        'end':False
    }
    path_cc = {
        'prompt': "you coped hard enough making you not suffer as much. in the end, it didn't matter :D",
        'end':True
    }

    def add(node, index, val):
        '''
            Purpose:
                Adds a node at the specified index which creates
                a linked list (or the illusion of one)
            Parameter(s):
                node: A node (dict)
                index: 'A', 'B', 'C' used to index our node (str)
                val: uses the 'path_' variables to determine 
                    the narration and its ending (dict)
            Return value:
                None
        '''
        node[index] = {"val": val, "A":None, "B":None, "C":None}
    
    # creation of the beginning node: 'start'
    root = {"val": path_start, "A": None, "B": None, "C": None}

    # 3 options added for: story -> ___
    add(root, 'A', path_a)
    add(root, 'B', path_b)
    add(root, 'C', path_c)

    # 3 options added for: story -> A -> ___
    add(root['A'], 'A', path_aa)
    add(root['A'], 'B', path_ab)
    add(root['A'], 'C', path_ac)

    # 3 options added for: story -> A -> C -> ___
    add(root['A']['C'], 'A', path_aca)
    add(root['A']['C'], 'B', path_acb)
    add(root['A']['C'], 'C', path_acc)

    # 3 options added for: story -> C -> ___
    add(root['C'], 'A', path_ca)
    add(root['C'], 'B', path_ac)
    add(root['C'], 'C', path_cc)

    # 3 options added for: story -> C -> B -> ___
    add(root['C']['B'], 'A', path_aca)
    add(root['C']['B'], 'B', path_acb)
    add(root['C']['B'], 'C', path_acc)

    # Main handler
    while root['val']['end'] == None:
        choice = three_options(root['val']['prompt'], root['val']['A'], root['val']['B'], root['val']['C'])
        root = root[choice]

    # we know that we've reached the bottom nodes, thus return node ending value
    print(f"\n{root['val']['prompt']}") 
    return root['val']['end']


        
if __name__ == '__main__':
    print(sound(6))  # Should output Yip
    print(sound(31)) # Should output Bark
    print(sound(30)) # Should output Ruff
    print(sound(71)) # Should output Boof

if __name__ == '__main__':
    print()
    print(sound2(13, True))  # Should output Meow
    print(sound2(50, False)) # Should output Bark
    print(sound2(111, True)) # Should output Meow 
    print(sound2(-1, False)) # Should output Yip

if __name__ == '__main__':
    print()
    choice = three_options("You don't know how to start this problem.",
        "Send an email to the TAs",
        "Go to office hours",
        "Post the problem online, there's no way I'll be caught")
    print("Return value: " + choice)

if __name__ == '__main__':
    print()
    choice2 = three_options("You must decide the fate of the galaxy.",
        "Destroy the robots",
        "Control the robots",
        "Merge with the robots?")
    print("Return value: " + choice2)

if __name__ == '__main__':
    print()
    choice3 = three_options("Choose a house.",
        "Black Eagles",
        "Slytherin",
        "Lannister")
    print("Return value: " + choice3)

if __name__ == '__main__':
    print()
    ending = adventure()
    print("Return value:", ending)
