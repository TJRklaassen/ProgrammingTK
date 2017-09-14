cijfers = {'Mark':9.4,'Bob':8.2,'Fabian':4.0,'Richard':6.5,'Freek':5.9,'Tim':9.1,'Jerry':3.5,'Tom':10.0}

for cijfer in cijfers:
    if cijfers[cijfer] > 9:
        print("{} heeft het cijfer: {}.".format(cijfer,cijfers[cijfer]))
