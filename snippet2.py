
import numpy as np

class Assignment2:
    def __init__(self):
        pass

    def intersections(self, f1: callable, f2: callable, a: float, b: float, maxerr=0.001) -> callable:
        """
     
        f1 : callable
            the first given function
        f2 : callable
            the second given function
        a : float
            beginning of the interpolation range.
        b : float
            end of the interpolation range.
        maxerr : float
            An upper bound on the difference between the
            function values at the approximate intersection points.


        Returns
        -------
        X : iterable of approximate intersection Xs such that for each x in X:
            |f1(x)-f2(x)|<=maxerr.

        """
        X=[]
        x_values = np.linspace(a,b)
        f1_y = [f1(val) for val in x_values]
        f2_y = [f2(val) for val in x_values]
        X = [(x_values[i]) for i,_ in enumerate(zip(f1_y,f2_y)) if f1_y[i] == f2_y[i]]
        return X



