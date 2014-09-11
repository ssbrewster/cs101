# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

from collections import Counter

def is_list(p):
    return isinstance(p, list)

def longest_repetition(reps):
    if reps == []:
        return None
    else:
        if is_list(reps[0]):
            longest_rep = Counter(x for sublist in reps for x in sublist)
            target_sub =  max(longest_rep, key = longest_rep.get)
            for i in reps:
                if i[0] == target_sub:
                    return i
        else:
            longest_rep = Counter(reps)
            return max(longest_rep, key = longest_rep.get)





#For example,

assert longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]) == 3
assert longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']) == 'b'
assert longest_repetition([1,2,3,4,5]) == 1
assert longest_repetition([]) == None



