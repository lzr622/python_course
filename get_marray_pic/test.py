a = input('数字:')
print(type(int(a)))
for s,i in enumerate(a):
    if i != '0':
        p = a[s:]
        print(int(p))

print('press<enter>')