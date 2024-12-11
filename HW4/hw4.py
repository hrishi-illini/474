from z3 import Bools, DeclareSort, Function, Consts, Const
from z3 import Or, And, Not, Exists, ForAll, Implies
from z3 import Solver, Tactic
# QE = Tactic('qe')   # quantifier elimination

G = DeclareSort('Group')
e, e1 = Consts('e e1', G)
f = Function('f', G, G, G)  # * 
g = Function('g', G, G)     # -1

conts = [e, e1]


# Group axioms
# (i)
ax1 = lambda x,y,z: f(f(x,y),z) == f(x,f(y,z))
# (ii)
ax2 = lambda x: And(f(x,e) == x, f(e,x) == x)
# (iii)
ax3 = lambda x: And(f(x,g(x)) == e, f(g(x),x) == e)


# Task 1: Prove that the identity element is unique
# Unque identity: (negation + skolemization)
u_id = lambda x: And(f(e1,x) == x, f(x,e1) == x, Not(e1 == e))


# The depth zero instantiations:
Task1_depth0 = []

for c1 in conts:
    for c2 in conts:
        for c3 in conts:
            Task1_depth0 = Task1_depth0 + [ax1(c1,c2,c3)]

for c in conts:
    Task1_depth0 = Task1_depth0 + [ax2(c), ax3(c), u_id(c)]

print('Task 1 Depth 0 instantiations:') 
for i in Task1_depth0:      
      print(i)
print('---Done Printing Task 1 Depth 0---')
print('Number of formulas afte to AND depth 0 instantiations:', len(Task1_depth0))  
print('Checking satisfiability of Task 1 depth 0 instantiations:')
s = Solver()
s.add(Task1_depth0)
if str(s.check()) == 'sat':
    print(s.model())    
else:
    print('unsat') 


# Task 2: Prove that the inverse element is unique
# # Group axioms
# # (i)
# ax1 = lambda x,y,z: f(f(x,y),z) == f(x,f(y,z))
# # (ii)
# ax2 = lambda x: And(f(x,e) == x, f(e,x) == x)
# # (iii)
# ax3 = lambda x: And(f(x,g(x)) == e, f(g(x),x) == e)


c, d= Consts('c d', G)
conts = [e, c, d]

# Unique inverse: (negation + skolemization)
u_inv = And(f(c,d) == e, f(d,c) == e, Not(d == g(c))) 


# The depth zero instantiations:
Task2_depth0 = []

for c1 in conts:
    for c2 in conts:
        for c3 in conts:
            Task2_depth0 = Task2_depth0 + [ax1(c1,c2,c3)]

for c1 in conts:
    Task2_depth0 = Task2_depth0 + [ax2(c1), ax3(c1)]

Task2_depth0 = Task2_depth0 + [u_inv]

print('Task 2 Depth 0 instantiations:') 
for i in Task2_depth0:      
      print(i)
print('---Done Printing Task 2 Depth 0---')   
print('Number of formulas to AND after depth 0 instantiations:', len(Task2_depth0)) 
print('Checking satisfiability of Task 2 depth 0 instantiations:')
s = Solver()
s.add(Task2_depth0)
if str(s.check()) == 'sat':
    # print(s.model())           # Depth 0 isn't enough.  Uncomment to see the model
    print('sat')       
else:
    print('unsat') 


# Adding depth 1 instantiations:
Task2_depth1 = []

depth0And1_terms = [e, c, d, g(e), g(c), g(d)]
for c1 in depth0And1_terms:
    for c2 in depth0And1_terms:
        for c3 in depth0And1_terms:
            Task2_depth1 = Task2_depth1 + [ax1(c1,c2,c3)]

for c1 in depth0And1_terms:
    Task2_depth1 = Task2_depth1 + [ax2(c1), ax3(c1)]

Task2_depth1 = Task2_depth1 + [u_inv]

print('Now using depth 1 as well.')
print('Checking satisfiability of Task 1 depth 0+1 instantiations:')
s = Solver()
s.add(Task2_depth1)
if str(s.check()) == 'sat':
    print(s.model())    
else:
    print('unsat') 