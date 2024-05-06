import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#from tkinter import *

'''top = Tk()
top.title("GRAPH THEORY")
top.geometry('500x450')
var = StringVar()
label = Label( top, textvariable=var, relief=RAISED )
var.set("ADJANCENCY MATRIX")
label.pack()
redButton = Button(top,text ="ADD",fg="red")
redButton.pack(side=TOP)
redButton = Button(top,text ="DELETE",fg="blue")
redButton.pack(side=TOP)
redButton = Button(top,text ="BACK",fg="green")
redButton.pack(side=TOP)
redButton = Button(top,text ="EXIT",fg="black")
redButton.pack(side=TOP)
top.mainloop()'''

R = int(input("Enter the number of rows:"))

C = int(input("Enter the number of columns:"))


print("Enter the entries in a single line (separated by space): ")


entries = list(map(int, input().split()))

matrix = np.array(entries).reshape(R, C)

print(matrix)

#B = np.matrix ([ [0,1,0,0,1,1],[1,0,1,0,0,1],[0,1,0,1,1,1],[0,0,1,0,0,0],[1,0,1,0,0,0],[1,1,1,0,0,0] ])
#A = {[1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 ]}
K = nx.from_numpy_matrix(matrix)

nx.draw(K,with_labels=1)

plt.show()
#0 1 1 0 0 1 1 0 0 1 1 0 1 0 0 1 1 0 0 1 1 0 0 1 0 1 1 0 0 1 1 0 0 1 1 0