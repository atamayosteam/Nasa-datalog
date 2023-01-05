import matplotlib.pyplot as plt
from collections import Counter

file = open('NASA_access_log_Jul95')
ip_addresses = []

try:
    for line in file:  
        ip_addresses.append(line.split(" ")[0])
       
except:
    print("uh-oh")

ip_counter = Counter(ip_addresses).most_common(10)
ip_values = []
ip_keys = []

print(ip_addresses)

c = Counter(ip_addresses)

newDict = dict()

for key, value in c.items():
    if value >=400: 
       newDict[key] = value 


print(newDict.keys())
print(newDict.values())

plt.bar(newDict.keys(),newDict.values())
plt.show()


