from z3 import Bools,  Ints, Reals
from z3 import Or, And, Not, Exists, ForAll, Implies
from z3 import Solver, Tactic
QE = Tactic('qe')   # quantifier elimination

x, y= Reals('x y')
phi = And( 2*y > 3*x, 4*y < 8*x + 10)

psi = ForAll( x, Exists(y, phi))

QE_psi = QE(psi)
print(QE_psi.as_expr())                   # Prints False
