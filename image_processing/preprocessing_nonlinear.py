from getImage import *
from MACHINE LEARNING MODEL import *
from preprocessing_lse import *
import matplotlib.pyplot as plt
import numpy as np
import math

#only for comparison
from scipy.optimize import curve_fit

image_path=r"C:\Users\Bose\Desktop\USC\projects\graphing_Project\graphing_Project\image_processing\tests\quadratic_test.jpg"
x_raw,y_raw=get_image(image_path)

structure=get_function(x_matrix,y_matrix)

x_fit,y_fit=np.zeros(len(x_matrix))

def applyNLfit(x_raw,x_fit,y_raw,y_fit):
    

while(math.abs(calculate_r2(y_raw,y_fit)>0)):
    applyNLfit(x_raw,x_fit,y_raw,y_fit)

plt.figure(figsize=(10,10))
plt.scatter(x_raw,y_raw)
plt.plot(x_fit,y_fit)
plt.plot(curve_fit(x_raw,y_raw))
plt.title("Raw vs Estimate vs Scikit vs Our fit")
plt.show()




