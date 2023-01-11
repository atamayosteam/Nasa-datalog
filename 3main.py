import matplotlib.pyplot as plt
from collections import Counter

myFile = open("NASA_access_log_Jul95")

ip_addresses = []
dates = []
directories = []

#How the code finds ip addresses, dates and file types.
try:
    for lines in myFile:
        x = lines.split(" ")[0]
        y = lines.split(" ")[3]
        y = y.split(":")[0]
        z = lines.split('"')[1]
        if '.' in z:
            z = z.split('.')[1]
            z = z.split(" ")[0]
        ip_addresses.append(x)
        dates.append(y)
        directories.append(z)

        
        
        #print(lines.split(" ")[0])
        
        #print("uh-oh")
except UnicodeDecodeError:
    print(lines)
    print("uh oh")
print(lines)
ip_counter = Counter(ip_addresses)
#Counter(ip_counter.most_common(3))


#Tells the user the most common ip addresses, dates, and file types.
print("The most frequent IP address was " + str(Counter(ip_addresses).most_common(3)))
print("The most frequent date was " + str(Counter(dates).most_common(4))) 
print("The most frequent file type was " + str(Counter(directories).most_common(7)))

fig, ax = plt.subplots()

# print(ip_counter.keys())
# print(ip_counter.values())


#Uses matplotlib to graph the most common IP addresses.
keyIP = []
valueIP = []

ip_counter = Counter(ip_addresses).most_common(20)

for ip in ip_counter:
   keyIP.append(ip[0])
   valueIP.append(ip[1])

plt.bar(keyIP, valueIP)

plt.xticks(rotation=30)

ax.set_title('Most Common DNS Addresses')
ax.set_xlabel('DNS Addresses')

plt.show()



#Uses matplotlib to graph the most common dates
keyTime = []
valueTime = []

Time_counter = Counter(dates).most_common()

for time in Time_counter:
   keyTime.append(time[0])
   valueTime.append(time[1])

plt.plot(keyTime, valueTime, marker='.', linestyle='-')

plt.xticks(rotation=30)

ax.set_title('Most Common Dates')
ax.set_xlabel('Dates')

plt.show()