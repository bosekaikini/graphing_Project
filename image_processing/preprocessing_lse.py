from getImage import *
import matplotlib.pyplot as plt
import numpy as np

image_path=r"C:\Users\Bose\Desktop\USC\projects\graphing_Project\graphing_Project\image_processing\tests\line_test.jpg"
x_matrix,y_matrix=get_image(image_path)


#LSE initial method
A=np.vstack([np.ones_like(x_matrix),x_matrix]).T
b=np.linalg.inv(A.T @ A) @ (A.T @ y_matrix)
intercept, slope=b

plt.figure(figsize=(10,10))
plt.scatter(x_matrix,y_matrix, color="blue",linewidth=1)
x=np.linspace(0, x_matrix.max())
y=x*slope + intercept
plt.plot(x,y, color="Red")
plt.title("Plot of least squares against all points")
plt.show()

#calculate r^2
def calculate_r2(y_matrix, y_expected):
    sum_squared_error=0
    sum_squared_total=0
    coefficient=(len(y_matrix)-1)/(len(y_matrix)-2)
    for i in range(0, 50):
        sum_squared_error+=(y_expected[i]-y_matrix[i])**2
        sum_squared_total+=y_matrix[i]**2
    return 1-coefficient*sum_squared_error/sum_squared_total


#output
print("Intercept: ",intercept)
print("Slope: ",slope)
print("r^2: ",calculate_r2(y_matrix,y))
