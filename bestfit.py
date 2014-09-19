import numpy as np
import matplotlib.pyplot as plt
import csv


def bestfit(DN):
    
    ax = np.array([0.0 for k in range (DN)])
    ay = np.array([0.0 for k in range (DN)])

    ll = 0
    file = open ("/Users/nauraj/Documents/Programs/scale_ht_comp/scale_ht_comp.csv","r")
    reader = csv.reader(file)
    for row in reader:
        x = row[0]
        ax[ll] = x
        y = row[1]
        ay[ll] = y
        #  print x,y
        ll = ll+1
    file.close()

    coff = np.polyfit(ax,ay,1)
    fn = np.poly1d(coff)
    print fn
    xp = np.linspace(0, 1, 100)
    plt.figure(1)
    plt.scatter(ax,ay)
    plt.plot(xp,fn(xp))
    plt.show()
    
    return
    
#bestfit(16)
