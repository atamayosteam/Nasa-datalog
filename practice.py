import matplotlib.pyplot as plt

plt.title('graph num 1')
x = list(range(0, 10))
y = list(range(-10, 0))

plt.plot(x, y)

plt.show()

plt.title('graph num 2')
a = [10, 2, 6, -3, 12]
b = [0, 3, 7, 3, 9]
plt.bar(a, b)
plt.show()

plt.title('graph num 3')
plt.hist(a)
plt.show()