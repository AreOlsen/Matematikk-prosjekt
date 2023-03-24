import pandas as pd
# Last inn data
fil = "torsk.csv"
datafil = pd.read_csv(fil, sep=",", comment="#", decimal=".")
codDataSet = datafil["TORSK"].tolist()
#Finn total mengde torsk som har levd.
total = 0
for i in codDataSet:
    total+=float(i)*1000 #Må gjere over frå '000 tonn til tonn.
print(f'Total mengde torsk målt er {total}tonn')