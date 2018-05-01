from sympy import oo
def wall_time(pos, vel, radius): return (1.0-radius-pos)/vel if vel>0.0 else (pos-radius)/abs(vel) if vel<0.0 else float(oo)
