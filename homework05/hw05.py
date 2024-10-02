import random

#DO NOT EDIT THE decrypt FUNCTION
#You're not required to understand how this works, but I've provided
#documentation to give you a general idea.
def decrypt(data, password):
    '''
    Purpose:
      Check whether the password is correct for a given encrypted
      file, and print out the decrypted contents if it is.
    Input Parameter(s):
      data is a string, representing the contents of an encrypted file.
      password is a four letter lowercase string, representing the password
      used to encrypt/decrypt the file contents.
    Return Value:
      Returns True if the password is correct and the file contents
      were printed.  Returns False and prints nothing otherwise.
    '''

    total = 0
    for ltr in password:
        total += ord(ltr)
        total *= 123
    encoded_pwd = pow(total,2011,547120141)
    
    data = data.split('\n')
    if encoded_pwd == int(data[0]):
        i = 0
        out_msg = ''
        for ltr in data[1]:
            out_msg += chr((ord(ltr)-ord(password[i]))%28 +97)
            i = (i+1)%len(password)
        out_msg = out_msg.replace('{',' ').replace('|','.')
        print(out_msg)
        return True
    return False


# Problem A: Spooky Numbers
def spooky(val):
    '''
    Purpose:
        Return True if the given integer is not divisible by
        integers through 10-31 inclusive
    Parameter(s):
        val : An integer (int)
    Return value:
        True if given integer is not divislbe by integers 10-31 inclusive
        False if given integer is divisible by integers 10-31 inclusive
    '''
    i = 10
    while 10 <= i <= 31:
        if val % i == 0:
            return False
        i += 1
    return True


# Problem B: Simulating a Sequence of Events
def four_tails():
    '''
    Purpose:
        Return the number of flips it takes to get
        4 tails in a row on a coin using the random function
    Parameter(s):
        None
    Return value:
        The number of flips it took to get 4 in a row. (int)
    '''
    i, flips = 0, 0
    while i < 4:
        flips += 1
        if random.randint(0,1) == 1:
            i += 1
            #print(f'Tails! {i} tails in a row.')
        else:
            i = 0
            #print(f'Heads! {i} tails in a row.')
    return flips


# Problem C: Estimating Sequence Probabilities
def average_four_tails(n):
    '''
    Purpose:
        Find the average of getting 4 tails in a row
        given an (n) amount of test cases.
    Parameter(s):
        n : The number of test cases to evaluate the avg (int)
    Return value:
        The likelihood of getting 4 tails in a row
        out of (n) attempts (float)
    '''
    total = 0
    for i in range(n):
        total += four_tails()
    return total/n
    

# Problem D: Brute Force Password Cracking
def find_password(filename):
    '''
    Purpose:
      Given an encrypted file, tries every possible four letter lowercase
      password for that file until one works, and then returns the password.
    Input Parameter(s):
      filename is a string representing the name of the encrypted file.
      The file must be in the same folder as this script.
    Return Value:
      Returns the password that successfully decrypts the given file
    '''
    fp = open(filename)
    data = fp.read()
    fp.close()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Initial Idea:
    # Given the alphabet, brute force 4 letter passwords given the lowercase alphabet
    # until a password is found that matches the encryption.

    # Second Idea:
    # Iterating through the alphabet and finding best fit can be down with
    # a two pointer approach.

    def check(password):
        '''
        Purpose:
            Converts password(list) to str to be used for the
            decryption comparion and returns True or False
        Parameter(s):
            password : The given 4 letter password (list)
        Return value:
            Returns True if encrypted data matches password (bool)
            Returns False if encrypted data does not match password (bool)
        '''
        password = ''.join(password)
        if decrypt(data, ''.join(password)):
            return True
        else:
            return False
        
    # Brute force method
    # Time complexity - O(26^4), 26 different options per character
    password = list('aaaa')
    for _ in range(0, 26):
        password[1] = 'a'
        for _ in range(0, 26):
            password[2] = 'a'
            for _ in range(0, 26):
                password[3] = 'a'
                for _ in range(0, 26):
                    password[3] = chr(ord(password[3]) + 1)
                    if check(password): return ''.join(password)
                password[2] = chr(ord(password[2]) + 1)
                if check(password): return ''.join(password)
            password[1] = chr(ord(password[1]) + 1)
            if check(password): return ''.join(password)
        password[0] = chr(ord(password[0]) + 1)
        if check(password): return ''.join(password)
    return False

if __name__ == '__main__':
    print(find_password('encrypted1.txt')) #Should output ford
    print()
    print(find_password('encrypted2.txt')) #Should output glad
    print()
    print(find_password('invalid.txt')) #Should output False
    print()

if __name__ == '__main__':
    print(spooky(35)) #Should output True
    print(spooky(31)) #Should output False
    print(spooky(1517)) #Should output True
    print(spooky(323)) #Should output False
    print(spooky(9)) # Should output True
    print(spooky(32)) # Should output False

if __name__ == '__main__':
    print()
    print(four_tails())
