import numpy as np
import matplotlib.pyplot as plt

x = np.arange(40, 44)
y = 75 - 4 ** (x-40)

plt.plot(x, y)
plt.show()