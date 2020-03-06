import csv
from password_strength import PasswordStats
dataset = open(r"Dataset/rockyou", "r", encoding='latin-1')
new_dataset = open("Dataset/Complexity3", "w", encoding='latin-1', newline='')
write = csv.writer(new_dataset,delimiter=',', quotechar='|', quoting=3)
write.writerow(["Password", "Complexity"])
for i in dataset:
    stats = PasswordStats(i)
    i=i.replace("\n", "")
    if stats.strength()<0.3:
        x=0
    elif stats.strength()<0.5:
        x=1
    elif stats.strength()<0.7:
        x=2
    else:
        x=3
    val = i + "," + str(stats.strength()) + ","+str(x)+","
    print(val)
    write.writerow([i, x])
new_dataset.close()