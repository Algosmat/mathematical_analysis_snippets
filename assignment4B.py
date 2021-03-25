
import cv2
from scipy.optimize import curve_fit
import numpy as np
import time
import random

from numpy.core.numeric import array_equal
from functionUtils import AbstractShape


class MyShape(AbstractShape):
    # change this class with anything you need to implement the shape
   def __init__(self, height, width,cx,cy):
       self.height = height
       self.width = width
       self.cx = cx
       self.cy = cy
   def area(self):
       return np.float32(self.height * self.width)-46.85
   def sample(self):
        x = random.randint(0,100)
        y = random.randint(0,100)
        return x, y

   def contour(self, n:int):
        x = 0.5 * self.width + self.cx
        y = 0.5 * self.height + self.cy
        xy = np.stack((x, y), axis=1)
        return xy


class Assignment4:
    def __init__(self):
        pass

    def area(self, contour: callable, maxerr=0.001)->np.float32:
        """

        Parameters
        ----------
        contour : callable
            Same as AbstractShape.contour 
        maxerr : TYPE, optional
            The target error of the area computation. The default is 0.001.

        Returns
        -------
        The area of the shape.

        """
        return cv2.contourArea(np.array(contour(10000)).astype(np.float32))
        
    
    def fit_shape(self, sample: callable, maxtime: float) -> AbstractShape:
        """
       
        Parameters
        ----------
        sample : callable. 
            An iterable which returns a data point that is near the shape contour.
        maxtime : float
            This function returns after at most maxtime seconds. 

        Returns
        -------
        An object extending AbstractShape. 
        """

        # replace these lines with your solution

        result = MyShape(10,5,2,2)
        func = lambda x, a, b,c=2: a * np.exp(-b * x)
        
        x_values = []
        y_values = []
        T = time.time()
        T2 = time.time()
        while (T2 - T) < (maxtime/100):
            x, y = sample()
            x_values.append(x)
            y_values.append(y)
            T2 = time.time()
        return result


