t1 = 1
t2 = 1
t3 = 1
print('B= 1,1,1', end =',')
for i in range(17):
    t4 = t1 + t2 + t3
    print(t4, end=',')
    t1,t2,t3 = t2,t3,t4