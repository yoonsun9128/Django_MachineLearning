import os

a = os.listdir('/titanic')

print(a)

for i in map(lambda x:x.split('.')[0], a):
    print(i)