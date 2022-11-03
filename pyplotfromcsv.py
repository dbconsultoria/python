import matplotlib.pyplot as plt
import numpy as np

dataArray = np.genfromtxt('C:\\Users\\Rodrigo\\Documents\\GitHub\\python\\sales.csv', delimiter=',', names=True)

plt.figure()
for col_name in dataArray.dtype.names:
    if col_name=='price':
        plt.plot(dataArray[col_name], 
            label=col_name)
plt.legend()
plt.show()