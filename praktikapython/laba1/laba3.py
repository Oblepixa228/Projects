import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20.01, 0.01)  
y = np.sin(x) * x**2          

plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, color='blue', label=r'$y(x) = \sin(x) \cdot x^2$')

plt.title('График функции $y(x) = \\sin(x) \\cdot x^2$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y(x)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

plt.show()