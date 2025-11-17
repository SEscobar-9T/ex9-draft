# working with sets
from pyscript import display


friends = {'Ross', 'Joey', 'Chandler', 'Monica', 'Rachel', 'Phoebe'} # specify sets
friends.add('Ben') # adding element
friends.remove('Chandler') # remove element
check_friends = 'Monica' in friends # checking item


display(friends, target='output1')
display(check_friends, target='output1')

# set operators
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

display(A | B, target='output2') # union
display(A.union(B), target='output2') # union
display(A - B, target='output2') # difference
display(A & B, target='output2') # intersection
display(A.intersection(B), target='output2') # intersection
display(A ^ B, target='output2') # symmetric difference
display(A.symmetric_difference(B), target='output2') # symmetric difference

# subset

display(A <= B, target='output3') # default subset
display(A < B, target='output3') # proper subset
display(A >= B, target='output3') # superset
display(A > B, target='output3') # proper superset

# frozenset

kats = frozenset(['Manon', 'Sophia', 'Lara', 'Daniela', 'Megan', 'Yoonchae'])

display(kats, target='output4')

