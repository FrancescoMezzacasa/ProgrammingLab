import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Grafico a Linee
x = np.linspace(-10, 10, 10)
y = [value**3 for value in x]

plt.plot(x, y)

plt.title('Grafico a Linee')
plt.xlabel('Asse x')
plt.ylabel('Asse f(x)')
plt.show()
