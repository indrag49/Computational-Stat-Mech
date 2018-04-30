from sympy import oo
import numpy as np
import math as m

def pair_time(pos_k, pos_l, vel_k, vel_l, radius):
        """ pos_k, pos_l, vel_k, vel_l all have two elements as a list """
        t_0=0.0
        pos_x=pos_l[0]-pos_k[0]
        pos_y=pos_l[1]-pos_k[1]
        Delta_pos=np.array([pos_x, pos_y])
        
        vel_x=vel_l[0]-vel_k[0]
        vel_y=vel_l[1]-vel_k[1]
        Delta_vel=np.array([vel_x, vel_y])

        Upsilon=(Delta_pos.dot(Delta_vel))**2-(Delta_vel.dot(Delta_vel))*((Delta_pos.dot(Delta_pos))-4*radius**2)

        if Upsilon>0.0 and Delta_pos.dot(Delta_vel)<0.0: return t_0-(Delta_pos.dot(Delta_vel)+m.sqrt(Upsilon))/(Delta_vel.dot(Delta_vel))
        else: return float(oo)