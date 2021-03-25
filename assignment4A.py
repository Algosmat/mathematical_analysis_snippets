
import numpy as np
import time


class Assignment4A:
    def __init__(self):
        pass

    def fit(self, f: callable, a: float, b: float, d:int, maxtime: float) -> callable:
        t0 = time.time()
        """
      
        f : callable. 
            A function which returns an approximate (noisy) Y value given X. 
        a: float
            Start of the fitting range
        b: float
            End of the fitting range
        d: int 
            The expected degree of a polynomial matching f
        maxtime : float
            This function returns after at most maxtime seconds. 

        Returns
        -------
        a function:float->float that fits f between a and b
        """

        def g(self):
              X = np.linspace(a,b,d)
              Y = f(X)
              #Phi = np.array([[xi,1] for xi in X])
              #Y = np.array([yi for yi in Y])
              x_mean = np.mean(X)
              y_mean = np.mean(Y)
              nume = 0
              denom = 0

              for i in range(len(X)):
                  nume += (X[i]-x_mean)*(Y[i]-y_mean)
                  denom += (X[i]-x_mean)**2
              m = nume/ denom
              c = y_mean - m *x_mean

              if (time.time() - t0) > maxtime + 5:
                  return [m, c]
        result = g
        y = f(1)
      

        return result

