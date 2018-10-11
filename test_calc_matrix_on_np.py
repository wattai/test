import numpy as np
import matplotlib.pyplot as plt

if __name__ is "__main__":
    a = np.random.randn(100, 32)
    b = np.random.randn(32, 1)

    c = a @ b
    print(c)

    plt.figure()
    plt.plot(c)
    plt.show()
