import csv
import matplotlib.pyplot as plt


class Plotter(object):
    
  def __init__(self,FN,DN):
      self.DN = DN
      self.FN = FN
    
    
  def my_plotter(self):

      ax = [[0.0 for k in range (self.DN)]for j in range(self.FN)]
      ay = [[0.0 for k in range (self.DN)]for j in range(self.FN)]
      
      for i in range(self.FN):
         st = str(i)
         jpt = 'data'+st
         ll = 0
         
         file = open ("/Users/nauraj/Documents/Programs/Data_files/"+jpt+".csv","r")
         reader = csv.reader(file)
         for row in reader:
                x = row[0]
                ax[i][ll] = x
                y = row[1]
                ay[i][ll] = y
                print x,y
                ll = ll+1
         file.close()
    
         plt.subplot(4,4,i)
         plt.figure(1)
         plt.scatter(ax[i],ay[i])
         plt.show()
         
      return
