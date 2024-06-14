import numpy as np
import matplotlib.pyplot as plt

date = np.arange(0, 1.1, 0.01)
plt.title('lines')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0, 1))
plt.ylim((0, 1))
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.plot(date, date ** 2)
plt.plot(date, date ** 4)
plt.legend(['y=x^2', 'y=x^4'])
plt.show()
