from z3 import Bools,  Ints, Reals, Real
from z3 import Or, And, Not, Exists, ForAll, Implies
from z3 import Solver, Tactic
QE = Tactic('qe')  # quantifier elimination

l1, l2, u1, u2, w, z = Reals('l1 l2 u1 u2 w z')

# Vertex set V, each vertex represented as a pair of reals (l, u)
V = {}
for i in range(1, 5):
    V[i] ={}
    V[i]['l'] = Real('l'+str(i))
    V[i]['u'] = Real('u'+str(i))

QuantG = [ V[i]['l'] for i in range(1, 5)] + [ V[i]['u'] for i in range(1, 5)]

# Edge relation
def IntervalEdge(i, j): # Edge(i,j) is true if the intervals overlap
    li, ui = V[i]['l'], V[i]['u']
    lj, uj = V[j]['l'], V[j]['u']
    return QE(Exists(z, And( li < z, z < ui, lj < z, z < uj))).as_expr()

# The graph:
Edges_G = [(1, 2), (1, 3), (2, 4), (3, 4)] + [ (i, i) for i in range(1, 5)] # The list on the left are the edges. 
                                                                            # The list on the right are the self loops (since any interval overlaps with itself)
NotEdge_G = []
for i in range(1, 5):
    for j in range(1, 5):
        if (i, j) not in Edges_G:
            NotEdge_G.append((i, j))
            
# G is an interval graph if exactly the edges in Edge_G satisfy the IntervalEdge relation
alphaG_fv = And( And([IntervalEdge(i, j) for i, j in Edges_G]), And([Not(IntervalEdge(i, j)) for i, j in NotEdge_G]))

alphaG = ForAll(QuantG, alphaG_fv)
QEalphaG = QE(alphaG).as_expr()
print(QEalphaG)             # prints False, so G is not an interval graph

# Same thing but calling a solver
s = Solver()
if str(s.check(QEalphaG)) == 'sat':
    print('Interval graph. Example:', s.model()) 
else:
    print('Not an Interval Graph')  

