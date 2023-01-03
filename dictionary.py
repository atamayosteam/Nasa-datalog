from collections import Counter
import matplotlib.pyplot as plt

fruits = [
        'apple','apple',
        'orange','orange','orange',
        'pear','pear','pear','pear',
        'grape','grape','grape','grape','grape'

]

fruit_counter= Counter(fruits)
print(fruit_counter.keys())
print(fruit_counter.values())

plt.bar(fruit_counter.keys(), fruit_counter.values())

plt.show()