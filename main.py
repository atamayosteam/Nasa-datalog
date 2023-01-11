import matplotlib.pyplot as plt
from collections import Counter


file = open('NASA_access_log_Jul95')
ip_addresses = []

try:
    for line in file:  
        ip_addresses.append(line.split(" ")[0])
       
except:
    print("uh-oh")

ip_counter = Counter(ip_addresses).most_common(1)

ip_values = []
ip_keys = []



c = Counter(ip_addresses)

newDict = dict()

for key, value in c.items():
    if value >=400: 
       newDict[key] = value 


print(newDict.keys())
print(newDict.values())

plt.bar(newDict.keys(),newDict.values(), color=['red', 'black',],)
plt.xticks(rotation= 30 )
plt.rcParams['font.size'] = 5
plt.ylabel("Num of times visited", size=15)
plt.title("Ip adresses ", size=18)



plt.show()





