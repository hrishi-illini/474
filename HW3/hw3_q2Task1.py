from z3 import Bools,  Ints, Reals
from z3 import Or, And, Not, Exists, ForAll, Implies
from z3 import Solver, Tactic
QE = Tactic('qe')  # quantifier elimination

l1, l2, u1, u2, w, z = Reals('l1 l2 u1 u2 w z')

# Forall z. ( A => Exists w. B)
B = And( l1 < w, w < u1, l2 < w, w < u2, Not(w == z))
A = And( l1 < z, z < u1, l2 < z, z < u2)

phi = ForAll( z , Implies(A, Exists(w, B)))
QE_phi = QE(phi)

print(QE_phi.as_expr())                   # Prints True