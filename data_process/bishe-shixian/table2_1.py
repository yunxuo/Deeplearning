import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
# y = (1/(1+np.exp(-x)))

# y = ((np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x)))

def ReLU(x):
    y = x.copy()
    y[y<0] = 0
    return y
# plt.figure(figsize=(4, 4))
y = ReLU(x)
plt.plot(x, y, label='$ReLU(x)$', color='blue', linewidth=1)


plt.xlabel('x')
plt.ylabel('ReLU(z)')
plt.title('ReLU')
plt.ylim(-5, 10)
plt.legend()

plt.show()