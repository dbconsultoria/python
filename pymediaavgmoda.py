import numpy
from scipy import stats

age = [18,19,55,65,33,45,18,56,45,50,60]

print('A média é ',numpy.mean(age))
print('A mediana é ',numpy.median(age))
print('A moda é ',stats.mode(numpy.array(age),keepdims=False))