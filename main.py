import matplotlib.pyplot as plt
from collections import Counter
file = open('NASA_access_log_Jul95')
ip_addresses = []

try:
    for line in file:  
        ip_addresses.append(line.split(" ")[0])
except:
    print("uh-oh")

ip_counter = Counter(ip_addresses)

c = Counter(ip_addresses)

print(ip_counter.keys())
print(ip_counter.values())

plt.bar(ip_counter.keys(), ip_counter.values())
plt.show()


