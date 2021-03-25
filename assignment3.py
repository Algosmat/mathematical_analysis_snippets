

import numpy as np
from assignment2 import Assignment2

class Assignment3:
    def __init__(self):
        pass

    def integrate(self, f: callable, a: float, b: float, n: int) -> np.float32:
        """   
        Parameters
        ----------
        f : callable. it is the given function
        a : float
            beginning of the integration range.
        b : float
            end of the integration range.
        n : int
            maximal number of points to use.

        Returns
        -------
        np.float32
            The definite integral of f between a and b
        """
        x = np.linspace(a,b,n)
        y = f(x)
        y_right = y[1:]
        y_left = y[:-1]

        dx = (b-a)/n
        A = (dx/2)**np.sum(y_right+y_left)
        result = np.float32(A)
        return result

    def areabetween(self, f1: callable, f2: callable) -> np.float32:
        """
        Parameters
        ----------
        f1,f2 : callable. These are the given functions

        Returns
        -------
        np.float32
            The area between function and the X axis

        """
        n = 100000
        X = Assignment2.intersections(f1,f2,0,100,100000)

        total_intersections = len(X)
        total_area1,total_area2,overall_area_sum = 0,0,0
        for i in range(total_intersections):
            if i < (total_intersections-1) and total_intersections > 1:
                total_area1 = self.integrate(f1,i,i+1,n)
                total_area2 = self.integrate(f2,i,i+1,n)
                overall_area_sum += abs(total_area1-total_area2)
        # replace this line with your solution
        result = np.float32(overall_area_sum)

        return result


