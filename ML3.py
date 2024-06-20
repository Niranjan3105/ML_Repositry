import pandas as pd
import matplotlib.pyplot as plt
import sklearn
file = 'cars2.xlsx'
df = pd.read_excel(file)
dictionary = df.to_dict()
#print(df)
#print(df.columns)
#print(df['total sulfur dioxide'])
a = df['Engine'].values
b = df['Power'].values
print(a)
print(b)
plt.scatter(a,b)
plt.show()
print('sklearn : {}'.format(sklearn.__version__))
#print(df.shape)
#print(df.describe())
#df.plot(kind ='box', subplots = True, layout = (12,12), sharex = False, sharey = False )
#plt.show()
#print(df.values)
#print(df.shape())


