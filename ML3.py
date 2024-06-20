import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
file = 'cars2.xlsx'
df = pd.read_excel(file)
dictionary = df.to_dict()
a = df['Engine'].values
b = df['Power'].values
# print(a)
# print(b)
# plt.scatter(a,b)
# plt.show()
mean_x = np.mean(a)
mean_y = np.mean(b)
m = len(a)
num = 0
denm = 0


for i in range(m):
    num += (a[i]-mean_x)*(b[i]-mean_y)
    denm += (a[i] - mean_x)**2

b1 = num/denm
b0 = mean_y - (b1*mean_x)
print(b1,b0)

max_a1 = np.max(a) + 200
min_a1 = np.min(a) - 200

a1 = np.linspace(max_a1,min_a1,1000)
a2 = b0 + b1*a1


plt.plot(a1,a2)
plt.scatter(a,b)
plt.title("Engine Volume vs power")
plt.xlabel("Engine cubic cm3")
plt.ylabel("Engine power")
plt.show()

#Calculate R square value

ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1*a[i]
    ss_t += (a1[i] - mean_y)**2
    ss_r += (a2[i] - y_pred)**2
    
r2 = 1 - (ss_r/ss_t)
print(r2)
    


