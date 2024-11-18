'''
1. What are the base cases of the merge function?
Why is the return value for those cases correct?

The base cases is if we have no more lists to go through thus
we simply just add the opposite hand side to our resulting list.

The return value for these cases are correct because we want
to conqueror back all the elements of our list.
If the element on the left is smaller, we will add it first
due to the natural ordering of lists. vice versa for the right side.

2. Describe what the recursive cases of merge are
doing to move towards the base case.

It's checking through the first element of a list
and comparing it to the first element of the other list
and recursively iterating using slicing.

3. What is the base case of the merge_sort function?
Why is the return value for that case correct?

The base case of the merge_sort function is if our
sequence is its own element. This means that we have
successfully divided all the elements into their own
'list' and can now merge them back together.

4. Describe what the recursive case of merge_sort 
does to move towards the base case.

It divides the lists in halves until they're their own
elements and can be regrouped by merging step by step.
'''

def merge(left, right):
    if left == '':  
        return right
    elif right == '':  
        return left
    elif left[0] <= right[0]:  
        return left[0] + merge(left[1:], right)
    else:  
        return right[0] + merge(left, right[1:])

def merge_sort(sequence):
    if len(sequence) <= 1:  
        return sequence
    else:
        left = sequence[:len(sequence)//2]  
        right = sequence[len(sequence)//2:]
        left = merge_sort(left)  
        right = merge_sort(right)
        return merge(left, right) 
    
def collatz(n):
    '''
    Purpose:
        Perform collatz conjecture on any given number
    Parameter(s):
        n : An integer (int)
    Return Value:
        The collatz conjecture sum (int)
    '''
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + collatz(n // 2)
    else:
        return n + collatz(n * 3 + 1)
    
def list_difference(list1, list2):
    '''
    Purpose:
        Subtract list1 from list2.
    Parameter(s):
        list1 : A list of integers (list)
        list2 : A list of integers (list)
    Return Value:
        The resulting list of list1 - list2
    '''
    if list1 == []:
        return []
    return [list1[0] - list2[0]] + list_difference(list1[1:], list2[1:])

def baking_contest(time_left, pastries):
    '''
    Purpose:
        Get the maximum number of points available
        within a given time limit for baked goods.
    Parameter(s):
        time_left : The amount of minutes left (int)
        pastries : The amount of pastries that can be made (list)
    Return Value:
        The most amount of points possible in the
        given time frame (int)
    '''

    # DFS Brute Force Approach
    # Time complexity: O(m^n) where m is the amount of pastries and n is
    # the maximum number of pastries able to be made in time_left minutes.
    if pastries == []:
        return 0

    maximum = 0
    for i in range(len(pastries)):
        if not (time_left - pastries[i][1] < 0):
            maximum = max(pastries[i][2] + baking_contest(time_left - pastries[i][1], pastries[:i] + pastries[i+1:]), maximum)
    return maximum
    


if __name__ == '__main__':
    print(merge_sort('')) #
    print(merge_sort('zany')) #anyz
    print(merge_sort('recursion')) #ceinorrsu

if __name__ == '__main__':
    print()
    print(collatz(5)) #Should return 36
    print(collatz(1)) #Should return 1
    print(collatz(123)) #Should return 6390

if __name__ == '__main__':
    print()
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
    #Should output 50 (real way) or 100 (easy way)
    #Gujiya + Taiyaki
    print(baking_contest(92, [['Gujiya', 55, 30],
                    ['Taiyaki', 35, 20],
                    ['Conejito', 60, 40],
                    ['Apple Strudel', 40, 10]]))

    #Should output 40 (real way) or 100 (easy way)
    #Conejito
    print(baking_contest(76, [['Gujiya', 55, 30],
                    ['Taiyaki', 35, 20],
                    ['Conejito', 60, 40],
                    ['Apple Strudel', 40, 10]]))  

    #Should output 88 (real way) or 142 (easy way)
    #Beaver Tail + Makmur + Pionono + Sfenj
    print(baking_contest(147, [['Alfajores', 30, 14],
                               ['Banket', 25, 16],
                               ['Beaver Tail', 50, 30],
                               ['Fa Gao', 55, 24],
                               ['Makmur', 45, 25],
                               ['Pionono', 22, 15],
                               ['Sfenj', 30, 18]]))

    #Should output 142 (real way) or 142 (easy way)
    #Enough time to get every pastry
    print(baking_contest(300, [['Alfajores', 30, 14],
                               ['Banket', 25, 16],
                               ['Beaver Tail', 50, 30],
                               ['Fa Gao', 55, 24],
                               ['Makmur', 45, 25],
                               ['Pionono', 22, 15],
                               ['Sfenj', 30, 18]]))

    #Should output 0 (real way) or 142 (easy way)
    #Not enough time for any pastries
    print(baking_contest(21, [['Alfajores', 30, 14],
                               ['Banket', 25, 16],
                               ['Beaver Tail', 50, 30],
                               ['Fa Gao', 55, 24],
                               ['Makmur', 45, 25],
                               ['Pionono', 22, 15],
                               ['Sfenj', 30, 18]]))
