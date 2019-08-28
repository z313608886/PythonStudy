import matplotlib.pyplot as plt
import pandas as pd
dc1 = pd.read_excel('静态抖动.xlsx',sheet_name='地磁场1')
dc2 = pd.read_excel('静态抖动.xlsx',sheet_name='地磁场2')
ct1 = pd.read_excel('静态抖动.xlsx',sheet_name='磁体1')
ct2 = pd.read_excel('静态抖动.xlsx',sheet_name='磁体2')
ct3 = pd.read_excel('静态抖动.xlsx',sheet_name='磁体3')
print(type(dc1))
print('地磁场1\nmin:\n%s\n' % dc1.min(),'\nmax:\n%s\n' % dc1.max())
print('地磁场2\nmin:\n%s\n' % dc2.min(),'\nmax:\n%s\n' % dc2.max())
print('磁体1\nmin:\n%s\n' % ct1.min(),'\nmax:\n%s\n' % ct1.max())
print('磁体2\nmin:\n%s\n' % ct2.min(),'\nmax:\n%s\n' % ct2.max())
print('磁体3\nmin:\n%s\n' % ct3.min(),'\nmax:\n%s\n' % ct3.max())

print(type(dc1.min()))
ct11=ct1.ix[:,2]
ct11.plot()
plt.show()
