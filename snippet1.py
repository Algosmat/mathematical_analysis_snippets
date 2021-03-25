
import numpy as np

class Assignment1:
    def __init__(self):
        pass

    def interpolate(self, f: callable, a: float, b: float, n: int) -> callable:
        """
        f : callable. it is the given function
        a : float
            beginning of the interpolation range.
        b : float
            end of the interpolation range.
        n : int
            maximal number of points to use.

        Returns the interpolating function
        """
        step = (b-a)/n
        x_values = np.array([a+step*diff for diff in range(n)])
        y_values = f(x_values)
        
        def result(xp):
            deno = (x_values-xp)**2
            return np.sum(y_values/deno)/np.sum(1/deno)
        return result






