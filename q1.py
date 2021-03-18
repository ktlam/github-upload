# version 1 (iterative approach): 
def get_length(p):
    q = p[::]
    count = 0
    while q:
        entry = q.pop()
        if isinstance(entry, list):
            q += entry
        else:
            count += 1
    return count

# version 2 (recursive approach): 
def get_length(lst):
    count = 0
    for entry in lst:
        if isinstance(entry, list):
            count += get_length(entry)
        else:
            count += 1
    return count

# version 3 (recursive approach): 
def get_length(lst):
    flat_list = []

    def flatten(lst):
        for item in lst:
            if type(item) == list:
                flatten(item)
            else:
                flat_list.append(item)
    
    flatten(lst)
    return len(flat_list)

'''
Note that version 2 and 3 define recursive functions to solve this problem.
We didn't teach recursion in this course and won't expect you can write such functions.
They are provided here for your future reference only.
'''

print(get_length([1, [2, 3]]))                          # prints 3 
print(get_length([1, [2, [3, 4]]]))                     # prints 4 
print(get_length([1, ['two'], 3, ['four'], 5]))         # prints 5 
print(get_length([1, [2, [3, ['a', ['b', 'c']]]]]))     # prints 6
