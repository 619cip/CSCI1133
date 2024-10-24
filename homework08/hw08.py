def remove_last(phrase):
    '''
    Purpose:
        Removes the last letter in each word of the phrase.
    Parameter(s):
        phrase : A sentence (str)
    Return Value:
        Returns the phrase with each last letter removed
        from each words (str)
    '''
    holder = []
    lst = phrase.split()
    for word in lst:
        holder.append(word[:-1])
    return ' '.join(holder)

def durdle_match(guess, target):
    '''
    Purpose:
        Return a hint sequence in regards of the target word.
    Parameter(s):
        guess : A user input to compare with the target word (str)
        target : The target word the user has to guess (str)
    Return Value:
        Return a combination of GYB hinting towards
        the completeness of the target word.
    '''
    res = [None] * len(guess)
    for i in range(len(guess)):
        if guess[i] == target[i]:
            res[i] = 'G'
        elif guess[i] in target:
            res[i] = 'Y'
        else:
            res[i] = 'B'
    return ''.join(res)

def durdle_game(target):
    '''
    Purpose:
        Compose a game for the user to guess the target word.
    Parameter(s):
        target : The target word to find (str)
    Return Value:
        The number of guesses it took to guess the word (int)
    '''
    print(f'Welcome to Durdle! The target word has {len(target)} letters.')

    res = ''
    tries = 0
    while res != 'G' * len(target):
        guess = input('Enter a guess:')
        if len(guess) != len(target) or not guess.isalpha() or not guess.islower():
            print('Invalid guess.')
            continue
        res = durdle_match(guess, target)
        print(f"{' ' * 15}{res}") # poor formatting
        tries += 1

    return tries

def get_genes(dna_string):
    '''
    Purpose:
        Get all the genes sequence given DNA sequence.
    Parameter(s):
        dna_string : a DNA sequence (str)
    Return Value:
        A list of genes found in the DNA sequence (list)
    '''

    genes = []
    dna_list = dna_string.split('ATG')
    stop_codon = ['TAG', 'TAA', 'TGA']
    for dna in dna_list:
        for codon in stop_codon:
            if codon in dna:
                genes.append(dna.split(codon)[0])
    return genes

if __name__ == '__main__':
    print(remove_last('one two three four five six')) #on tw thre fou fiv si
    print(remove_last('hey i am a cs major')) # he  a  c majo
    print(remove_last('coding is fun')) # codin i fu

if __name__ == '__main__':
    print()
    print(durdle_match('quick', 'perky')) #BBBBY
    print(durdle_match('test','deft')) #YGBG
    print(durdle_match('wizard','zicron')) #BGYBYB
    print(durdle_match('parry','perky')) #GBGYG
    print(durdle_match('guessing','guessing')) #GGGGGGGG

if __name__ == '__main__':
    print()
    tries = durdle_game('trick')
    print(f'Number of guesses: {tries}')

if __name__ == '__main__':
    print()
    tries = durdle_game('parameter')
    print(f'Number of guesses: {tries}')

if __name__ == '__main__':
    print()
    print(get_genes("TCATGTGCCCAATTCTGACCTACGATGGCCCAATAGCG"))
    #["TGCCCAATTC", "GCCCAA"]

    print(get_genes('ATTGCGCTACGCATC'))
    #[]

    print(get_genes('CATGTGTGAC'))
    #['TG']

    print(get_genes('ATGGTATCGTAAGATGGGGGTAGATATGTGA'))
    #['GTATCG', 'GGGG', '']

