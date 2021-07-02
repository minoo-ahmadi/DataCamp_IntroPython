## numpy.random.normal generates random data
# Arguments: distribution mean, distribution standard deviation, number of samples.
# Example:
import numpy as np
height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack ((height, weight))
bmi = weight/height**2

# np.round has 2 arguments: number is mandatory and ndigits is optional
#(if left out an integer is returned). help(round) for more info.
# column_stack is the equal of cbind in R.

## Some basic statistical operations on the data:
np_city_mean = np.mean(np_city)
np_city_std = np.std(np_city)
np_city_median = np.median(np_city)

#print(np_city_std)

import matplotlib.pyplot as plt
plt.plot(weight, bmi)
plt.show()

#plt.scatter(height, bmi)
#plt.show()

