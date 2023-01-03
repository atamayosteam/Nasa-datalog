import matplotlib.pyplot as plt

categories = ['apples', 'bannana', 'pear', 'oranges', 'kiwi' ]
numbers = [2, 4, 5, 2, 9]

plt.bar(categories, numbers, color=['red', 'yellow', 'green', 'orange', 'brown'])
plt.show()