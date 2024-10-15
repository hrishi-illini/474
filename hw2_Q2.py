from z3 import Bool, Or, And, Not
from z3 import Solver


p = Bool('p')
q = Bool('q')
r = Bool('r')

# Clauses in phi:
q_notr = Or(q, Not(r))
notp_r = Or(Not(p), r)
notq_r_p = Or(Not(q), r, p)
p_q_notq = Or(p, q, Not(q))
notr_q = Or(Not(r), q)

# Clauses the Resolved Set:
# q_notr
# notp_r
# notq_r_p
q_notp = Or(q, Not(p))
r_notq = Or(r, Not(q))


phi = And(q_notr, notp_r, notq_r_p, p_q_notq, notr_q)
res_phi = And(q_notr, notp_r, notq_r_p, q_notp, r_notq)  # Note: It's possible that the resolved set res_phi is over a smaller set of variables than phi.
                                                         # But since res_phi is constructed by discarding tautologies..... v |= phi iff (v restricted to vars(res_phi)) |= res_phi.
                                                        # Example: p V ~p gets resolved (modulo tautologies) to true.

s = Solver()

s.add(phi)
if str(s.check()) == 'sat':
    print('phi is sat:', s.model())
else:
    print('phi not sat')

s = Solver()
s.add(Not(phi == res_phi))

if str(s.check()) == 'sat':
    print('phi not equivalent to res_phi:', s.model())
else:
    print('phi == res_phi')      # (2d): unsat