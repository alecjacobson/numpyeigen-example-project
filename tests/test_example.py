from example import example_function
import numpy as np

A_python = np.array([0.5, 0.1, 10.])
B_python = np.array([[0., 1., 2.],[3., 4., 5.]])
print("B_python:\n", B_python)
example_function(A_python,B_python)
