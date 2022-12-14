file = open('NASA_access_log_Jul95')
ip_adresses = []

try:
    for line in file:  
        print(line.split(" ")[0])
except:
    print("uh-oh")
