def box_it(X, L):
        """X is a vector of x and y coordinates of a hard disk"""
        """L is a vector of Lx and Ly, such that the box has size Lx X Ly"""
        return [X[0]%L[0], X[1]%L[1]]

def diff_vec(X1, X2, L):
        """X1 and X2 are the position coordinates of the two hard disks"""
        Delta_x=[X1[0]-X2[0], X1[1]-X2[1]]
        X_Delta, Y_Delta=box_it(Delta_x, L)
        print X_Delta, Y_Delta
        if X_Delta>L[0]/2.: X_Delta-=L[0]
        if Y_Delta>L[1]/2.: Y_Delta-=L[1]
        return [X_Delta, Y_Delta]