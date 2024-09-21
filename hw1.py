from z3 import Bool, Or, And, Not
from z3 import Solver


P = ['a', 'b', 'c']
D = ['u', 'v', 'w', 'x', 'y', 'z']

Ddict = {}
Edict = {}

Ddict['a'] = ['u', 'v', 'w', 'x', 'y', 'z']
Ddict['b'] = ['y', 'z']
Ddict['c'] = ['w', 'x']

for d in D:
    Edict[d] = []
Edict['v'] = ['x'] # Q2 part (c)
# Edict['v'] = ['u'] # Uncomment this for part (d)

# PropNames will be populated with all propostions. Prop pd is true means p adopts d.
PropNames = {}
for p in P: # For each person p and dog d...
    for d in D:
        PropNames[p + d] = Bool(p + d) # create proposition pd - 'p adopts d'.

# Each person wants at least 2 dogs.
Want = []
for i in P: # For each person i and two (different) dogs d, d1....
    iwant = []
    for d in Ddict[i]:
        for d1 in Ddict[i]:
            if d1 != d:
                iwant.append(And(PropNames[i+d], PropNames[i+d1])) # i adpots d and d1 (d != d1)
    Want.append(Or(iwant)) # i adopts some d, d1 

# No person shares a dog with another person.
NoSharing = []
for i in P: # For person i,j and a dog d.....
    for j in P:
        if i != j:
            for d in D:
                NoSharing.append(Not(And(PropNames[i+d], PropNames[j+d]))) # both i and j cannot adopt d

# No person adopts two dogs that are in conflict.
NoConflict = []
for d in D: # For each dog d and e confliicting with d...
    for e in Edict[d]:
        for p in P:
            NoConflict.append(Not(And(PropNames[p+d], PropNames[p+e]))) # p cannot adopt both d and e


s = Solver()
s.add(Want)
s.add(NoSharing)
s.add(NoConflict)

if str(s.check()) == 'sat':
    print(s.model())    # (2c): sat model: a-adopts->(v,u), b->(y,z), c->(w,x)
else:
    print('unsat')      # (2d): unsat
