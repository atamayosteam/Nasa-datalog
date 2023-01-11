from collections import *
import matplotlib.pyplot as plt

File= open("NASA_access_log_Jul95")
plt.style.use("dark_background")

dates=[]

try:
    for lines in File:
        time=lines.split(' ')[3]
        time=time.split(':')[0]
        time=time.split('[')[1]
        time=time.split('/1995')[0]
        dates.append(time)
except UnicodeDecodeError:
    print('uhooh')

time_date= Counter(dates).most_common(10)
dateKeys = Counter(dates).keys()
timevalues = Counter(dates).values()
print(dateKeys)
print(timevalues)
date_value=[]
date_key=[]

fig, ax = plt.subplots()

for z in time_date:
    date_key.append(z[0])
    date_value.append(z[1])


plt.plot(dateKeys,timevalues,
    color='green',
    marker="o",
    )

plt.xticks(rotation=30)

ax.grid(color='red') 
plt.xlabel("Date")
plt.ylabel("Searches on Day")

plt.show()

print(f"The most frequent date was {Counter(time).most_common(1)}")
