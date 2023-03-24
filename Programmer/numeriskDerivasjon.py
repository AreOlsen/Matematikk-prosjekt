import pandas as pd
import matplotlib.pyplot as plt
# Last inn data
fil = "torsk.csv"
datafil = pd.read_csv(fil, sep=",", comment="#", decimal=".")
yakse = datafil["TORSK"].tolist()
#Liste over modell data.
xVerdier=[]
yDerivertVerdier=[]
#Teikne diagram over målte data.
for i in range(len(yakse)):
    xVerdier.append(i)
    yakse[i]=yakse[i]*1000 #Frå '000 tonn til tonn.
plt.plot(xVerdier,yakse,"x")
#Modeller den deriverte.
for x in range(len(yakse)-1):
    derivert = yakse[x+1]-yakse[x] #(yf-yi)/(xf-xi) xf-xi=1
    print(derivert)
    yDerivertVerdier.append(derivert)
#Vis derivert saman med målte data.
xVerdier.pop()
plt.grid()
plt.plot(xVerdier,yDerivertVerdier)
plt.xlabel("År etter 1987.")
plt.ylabel("Torskmengde.")
plt.show()