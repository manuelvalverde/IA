from numpy import load

data = load('traj.npz')
lst = data.files

i = 0
for item in lst:
    print(item)
    #print(data[item])
    for x in data[item]:
        if x[0] == 6:
            print(x)
