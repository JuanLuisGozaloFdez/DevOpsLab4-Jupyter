import matplotlib.pyplot as plt
x = range(1000)
y = [i ** 2 for i in x]
plt.plot(x,y)
plt.show()