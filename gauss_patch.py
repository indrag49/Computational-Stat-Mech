import random
import math as m

def gauss_patch(sigma):
        while True:
                x=random.uniform(-1, 1)
                y=random.uniform(-1, 1)
                Upsilon_dashed=x**2+y**2
                if (Upsilon_dashed>1 or Upsilon_dashed==0): continue
                else: break
        Upsilon=-m.log(Upsilon_dashed)
        Upsilon_double_dashed=sigma*m.sqrt(2*Upsilon/Upsilon_dashed)
        x=Upsilon_double_dashed*x
        y=Upsilon_double_dashed*y
        return [x, y]