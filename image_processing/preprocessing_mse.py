from getImage import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

image_path=image_path=r"C:\Users\Bose\Desktop\USC\projects\graphing_Project\graphing_Project\image_processing\tests\line_test.jpg"
x_matrix,y_matrix=get_image(image_path)


#Linear Regression pack scipy
slope, intercept, r, p, std_err = stats.linregress(x_matrix, y_matrix)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x_matrix))

#output
print("Intercept: ",intercept)
print("Slope: ",slope)

#plotting both on the same graph
plt.figure(figsize=(10,10))
plt.scatter(x_matrix,y_matrix, color="blue",linewidth=1)
x=np.linspace(0, x_matrix.max())
plt.plot(x,mymodel, color="Red")
plt.title("Plot of least squares against all points")
plt.show()